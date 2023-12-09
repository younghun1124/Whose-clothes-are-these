import os
import cv2
import numpy as np
import torch
import torch.nn as nn
from torchvision import models, transforms

# Function to extract features using a pre-trained ResNet model
def extract_resnet_features(image_path, model):
    img_array = np.fromfile(image_path, np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR) #cv.imread 한글 경로 인식 안되는 문제를 해결하기 위해 넘파이 array로 먼저 받아오기    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    image = cv2.resize(image, (224, 224))  # Resize to match ResNet input size
    image = transforms.ToTensor()(image).unsqueeze(0)  # Convert to PyTorch tensor
    image = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])(image)  # Normalize
    features = model(image)
    return features.flatten().detach().numpy()

# Load pre-trained ResNet model for feature extraction
model = models.resnet50(pretrained=True)
model = nn.Sequential(*list(model.children())[:-1])

# Set the model to evaluation mode
model.eval()

# Define the folder containing pre-stored clothing photos
current_script_directory = os.getcwd()
folder_path = os.path.join(current_script_directory, 'images2')


# Load and extract features for pre-stored clothing photos
pre_stored_features = {}
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    image_features = extract_resnet_features(file_path, model)
    pre_stored_features[file_name] = image_features

# Define the target clothing photo
target_photo_path = os.path.join(current_script_directory, 'target.jpg')

# Extract features for the target clothing photo
target_features = extract_resnet_features(target_photo_path, model)

# Calculate similarity between the target photo and pre-stored photos
similarities = {}
for file_name, features in pre_stored_features.items():
    similarity = np.dot(target_features, features) / (np.linalg.norm(target_features) * np.linalg.norm(features))
    similarities[file_name] = similarity

# Find the closest pre-stored clothing photo
closest_photo = max(similarities, key=similarities.get)
similarity_score = similarities[closest_photo]
ranked_photos = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
for rank, (photo, similarity_score) in enumerate(ranked_photos, start=1):
    print(f"Rank {rank}: {photo} (Similarity Score: {similarity_score})")