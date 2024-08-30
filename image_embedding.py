import torch
from transformers import CLIPProcessor, CLIPModel
import pickle
import torch.nn.functional as F

# Load the CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("./TBIR_model").to(device)
processor = CLIPProcessor.from_pretrained("./TBIR_processor")


def extract_category_from_filename(filename):
    # the category is part of the filename like "bottom" or "top"
    if "top" in filename:
        return "top"
    elif "bottom" in filename:
        return "bottom"
    else:
        return None  # might handle other categories such as dress in the future


def retrieve_images_for_query_random(model, processor, text_query, top_k=10, top_limit=3, bottom_limit=3, temperature=1.0):
    with open("./processed_images.pkl", 'rb') as f:
        images, image_files = pickle.load(f)

    # Process the images and text query
    inputs = processor(text=[text_query], images=images,
                       return_tensors="pt", padding=True).to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    # Since we have only one text query, the first element is taken
    logits_per_text = outputs.logits_per_text[0]

    # Apply temperature to logits for more randomness
    logits_per_text = logits_per_text / temperature

    # Convert logits to probabilities
    probs = F.softmax(logits_per_text, dim=-1)

    # Sample top-k indices based on probabilities
    top_k_indices = torch.multinomial(probs, num_samples=top_k)

    top_count = 0
    bottom_count = 0
    results = []

    for idx in top_k_indices:
        idx = idx.item()
        filename = image_files[idx]
        # Extract "top" or "bottom" from filename
        category = extract_category_from_filename(filename)

        if category == "top" and top_count < top_limit:
            results.append(filename)
            top_count += 1
        elif category == "bottom" and bottom_count < bottom_limit:
            results.append(filename)
            bottom_count += 1

        # Break if both limits are reached
        if top_count >= top_limit and bottom_count >= bottom_limit:
            break

    return results
