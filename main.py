import cv2
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

def extract_color_histogram(image_path):
    image = cv2.imread(image_path)
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(histogram, histogram)
    return histogram.flatten()

# Load images and extract features
image_paths = ['path/to/image1.jpg', 'path/to/image2.jpg', '...']
features = np.array([extract_color_histogram(path) for path in image_paths])

# Clustering
kmeans = KMeans(n_clusters=3)  # Adjust the number of clusters
labels = kmeans.fit_predict(features)

# Visualize the results
for i in range(len(labels)):
    plt.subplot(1, len(labels), i + 1)
    plt.imshow(cv2.imread(image_paths[i]))
    plt.title(f'Cluster {labels[i]}')
    plt.axis('off')
plt.show()
