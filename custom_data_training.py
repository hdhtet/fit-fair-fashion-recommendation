from PIL import Image
import json
import os
import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from torch.optim import AdamW
from torch.nn import CrossEntropyLoss
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


class CustomDataset(Dataset):
    def __init__(self, json_file, img_dir, processor):
        with open(json_file, 'r') as f:
            self.annotations = json.load(f)
        self.img_dir = img_dir
        self.processor = processor

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        img_info = self.annotations[idx]
        img_path = os.path.join(self.img_dir, img_info['filename'])
        image = Image.open(img_path).convert("RGB")
        text = img_info['description']

        inputs = self.processor(
            text=[text], images=image, return_tensors="pt", padding=True)

        # Return individual tensors rather than a dictionary with tensors
        return inputs['input_ids'].squeeze(0), inputs['pixel_values'].squeeze(0), inputs['attention_mask'].squeeze(0)


def collate_fn(batch):
    input_ids = [item[0].squeeze(0) for item in batch]
    pixel_values = [item[1].squeeze(0) for item in batch]
    attention_mask = [item[2].squeeze(0) for item in batch]

    # Pad the input_ids and attention_mask
    input_ids = torch.nn.utils.rnn.pad_sequence(
        input_ids, batch_first=True, padding_value=processor.tokenizer.pad_token_id)
    attention_mask = torch.nn.utils.rnn.pad_sequence(
        attention_mask, batch_first=True, padding_value=0)

    pixel_values = torch.stack(pixel_values)

    return {
        "input_ids": input_ids,
        "pixel_values": pixel_values,
        "attention_mask": attention_mask
    }


dataset = CustomDataset(json_file="./train_data.json",
                        img_dir="./static/images/SAH Project.v2i.clip/train", processor=processor)
dataloader = DataLoader(dataset, batch_size=32,
                        shuffle=True, collate_fn=collate_fn)


def make_contiguous(model):
    for name, param in model.named_parameters():
        if not param.is_contiguous():
            param.data = param.contiguous()

# Training Loop


optimizer = AdamW(model.parameters(), lr=5e-5)
loss_fn = CrossEntropyLoss()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

num_epochs = 35

model.train()
for epoch in range(num_epochs):
    for batch in dataloader:
        inputs = {key: value.to(device) for key, value in batch.items()}

        # Forward pass
        outputs = model(**inputs)

        logits_per_image = outputs.logits_per_image
        logits_per_text = outputs.logits_per_text

        ground_truth = torch.arange(len(logits_per_image)).to(device)
        loss_image = loss_fn(logits_per_image, ground_truth)
        loss_text = loss_fn(logits_per_text, ground_truth)

        loss = (loss_image + loss_text) / 2

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}")

make_contiguous(model)
model.save_pretrained("./TBIR_model")
processor.save_pretrained("./TBIR_processor")
