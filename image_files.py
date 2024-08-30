import pickle
from PIL import Image
import os
import json

# Process images and save them along with their file paths
def process_and_save_images(image_dir, pickle_file='processed_images.pkl'):
    with open("./train_data.json", 'r') as f:
        json_data = json.load(f)

    image_files  = [os.path.join(image_dir ,file['filename']) for file in json_data]
    images = [Image.open(image_file).convert('RGB') for image_file in image_files]

    # Save the processed images and image files as a pickle file
    with open(pickle_file, 'wb') as f:
        pickle.dump((images, image_files), f)
    
    print(f"Processed images and file paths saved as '{pickle_file}'")


# usage
image_dir  = "static/images/SAH Project.v2i.clip/train"
process_and_save_images(image_dir)
