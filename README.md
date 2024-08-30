# fit-fair-fashion-recommendation
FitFair - Fashion Recommendation System Based on Body Shape
* Hackathon Project Overview
This project is a cutting-edge AI-powered fashion recommendation system designed to offer personalized clothing suggestions based on an individual's body shape. The system leverages AI to accurately identify body shapes and provides tailored fashion advice, including recommendations for casual and formal outfits, complete with top and bottom pairings.


* Key Features
AI-Powered Body Shape Identification: Utilizes the OpenAI API to analyze and determine the user's body shape with precision.
Personalized Fashion Recommendations: Suggests outfits that best complement the identified body shape, including options for both casual and formal wear.
Comprehensive Outfit Pairing: Delivers complete outfit suggestions, including tops and bottoms, to enhance the user’s fashion sense.


* Quick Start Guide
1. Clone the Repository
Begin by cloning the project repository to your local machine:
git clone https://github.com/hdhtet/fit-fair-fashion-recommendation.git
cd fashion-recommendation-system

2. Set Up the Environment
To ensure consistency and avoid dependency issues, it's recommended to use a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies
Install all the necessary Python packages listed in requirements.txt:
pip install -r requirements.txt

4. Download and Train the AI Model
To download the pre-trained model and perform custom training, execute the following:
python custom_data_training.py
This script will handle the model download and initiate the training process using your custom data, ensuring the AI is fine-tuned for optimal performance.

5. Generate Image Files
Prepare the pickled image files required by the system by running:
python image_files.py
This step processes the images and saves them in a format that the system can efficiently utilize.

6. Launch the Application
Finally, start the web application to interact with the system:
python app.py
The application will launch in your default web browser, where you can begin uploading images or entering data to receive personalized fashion recommendations.

* How It Works
Upload or Input Data: Users can either upload an image or input their body shape manually.
AI Analysis: The system uses AI to analyze the data and identify the user’s body shape.
Get Recommendations: Based on the analysis, the system suggests the most suitable outfits, both casual and formal.
Interactive Experience: Users can explore various outfit suggestions, customize preferences, and save favorite looks. (future implementations)


* Project Structure
├── app.py                        # Entry point of the web application
├── custom_data_training.py       # Script to download and fine-tune the AI model
├── image_embedding.py            # Script to retrieve images based on text query using CLIP
├── image_files.py                # Script to process and pickle image files
├── requirements.txt              # Dependency list
├── README.md                     # Project documentation (this file)
├── static/                       # Static assets (images, CSS, JS, etc.)
├── templates/                    # HTML templates for the UI
└── TBIR_model/                   # Directory for trained models and assets
!!! processed_images.pkl file not pushed to git due to large storage !!!


* Technologies Used
Python
OpenAI API: For advanced AI-based body shape identification.
PIL (Python Imaging Library): For image processing tasks.
Flask: As the web application framework.
PyTorch/TensorFlow: For model training and inference.


* Why This Project?
This AI hackathon project showcases how AI can be applied to solve real-world problems in the fashion industry. By combining body shape identification with personalized clothing recommendations, this system provides a unique and practical solution for enhancing personal style and confidence.


Team Name: InnoVentures
Project Name: Fashion Recommendation System
Product Name: FitFair
