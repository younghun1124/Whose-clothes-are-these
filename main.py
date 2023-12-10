import os
import cv2
import numpy as np
import torch
import torch.nn as nn
from torchvision import models, transforms
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify,render_template,send_from_directory

app = Flask(__name__)

# Function to extract features using a pre-trained ResNet model
def extract_resnet_features(image):
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
    img_array = np.fromfile(file_path, np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR) #cv.imread 한글 경로 인식 안되는 문제를 해결하기 위해 넘파이 array로 먼저 받아오기    
    image_features = extract_resnet_features(image)
    pre_stored_features[file_name] = image_features

@app.route('/images2/<filename>')
def send_image(filename):
    return send_from_directory("images2", filename)
@app.route('/upload', methods=['POST'])
def upload_image():
    print("Route hit")  # Debugging
    try:
        target_image = request.files['fileToUpload']
        print("File received:", target_image.filename)  # Debugging
        name_option = request.form['nameSelect']

        if target_image:
            filename = secure_filename(target_image.filename)
            base_name, file_extension = os.path.splitext(filename)

            # 이미지 이름 생성 (중복 처리)
            counter = 1
            new_filename = f"{name_option}{file_extension}"
            while os.path.exists(os.path.join(folder_path, new_filename)):
                new_filename = f"{name_option}_{counter}{file_extension}"
                counter += 1

            # 이미지 저장
            save_path = os.path.join(folder_path, new_filename)
            target_image.save(save_path)

            # 추가 로직 ...

            return "File uploaded and saved!"

    except Exception as e:
        return str(e)
@app.route('/compare', methods=['POST'])
def upload_target_image():
    try:
        target_image = request.files['fileToUpload']
        if target_image:
            # Convert uploaded image to numpy array
            target_image_data = np.frombuffer(target_image.read(), np.uint8)
            target_image = cv2.imdecode(target_image_data, cv2.IMREAD_COLOR)

            # Extract features for the target clothing photo
            target_features = extract_resnet_features(target_image)

            # Calculate similarity between the target photo and pre-stored photos
            similarities = {}
            for file_name, features in pre_stored_features.items():
                similarity = np.dot(target_features, features) / (np.linalg.norm(target_features) * np.linalg.norm(features))
                similarities[file_name] = similarity

            # 유사도 순으로 정렬
            ranked_photos = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
            response_data = [{"photo": photo, "similarity_score": float(score)} for photo, score in ranked_photos]

            # HTML 템플릿 렌더링
            return render_template('results.html', results=response_data)

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)