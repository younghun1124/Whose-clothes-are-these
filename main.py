import cv2
import numpy as np
import os
from scipy.spatial.distance import cosine

def extract_color_histogram(image_path):
    
    img_array = np.fromfile(image_path, np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR) #cv.imread 한글 경로 인식 안되는 문제를 해결하기 위해 넘파이 array로 먼저 받아오기
    
    
    if image is None:
        raise ValueError(f"Unable to load image at path: {image_path}")
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(histogram, histogram)
    return histogram.flatten()

def compare_histograms(hist1, hist2):
    return cosine(hist1, hist2)
current_script_directory = os.getcwd()
# Specify the folder path
folder_path = os.path.join(current_script_directory, 'images')
target_path = os.path.join(current_script_directory, 'target.jpg')
# Retrieve and filter image files
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]

# Extract histograms
histograms = [extract_color_histogram(path) for path in image_paths]
target_histogram = extract_color_histogram(target_path)

# Compare each image with the target
similarities = [compare_histograms(target_histogram, histogram) for histogram in histograms]

# Find the most similar image
most_similar_image_index = np.argmin(similarities)
print(f"The most similar image to target is: {image_paths[most_similar_image_index]} with a similarity score of {similarities[most_similar_image_index]}")