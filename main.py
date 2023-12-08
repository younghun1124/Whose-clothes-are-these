import cv2
import numpy as np
from scipy.spatial.distance import cosine
from itertools import combinations

def extract_color_histogram(image_path):
    image = cv2.imread(image_path)
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(histogram, histogram)
    return histogram.flatten()

def compare_histograms(hist1, hist2):
    return cosine(hist1, hist2)

# Paths to your images
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg', ...]

# Extract histograms
histograms = [extract_color_histogram(path) for path in image_paths]

# Compare each pair of images
pairs = combinations(range(len(histograms)), 2)
similarities = {pair: compare_histograms(histograms[pair[0]], histograms[pair[1]]) for pair in pairs}

# Find the most similar pair
most_similar_pair = min(similarities, key=similarities.get)
print(f"The most similar images are: {image_paths[most_similar_pair[0]]} and {image_paths[most_similar_pair[1]]} with a similarity score of {similarities[most_similar_pair]}")
