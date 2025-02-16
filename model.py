import os
import cv2
import numpy as np
from sklearn.neighbors import NearestNeighbors

def extract_features(image_path):
    """Extract features from an image using OpenCV"""
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize image to fixed size
    img = cv2.resize(img, (128, 128))
    
    # Apply histogram equalization
    img = cv2.equalizeHist(img)
    
    # Flatten the image to create feature vector
    features = img.flatten()
    
    # Normalize features
    features = features / 255.0
    
    return features


def train_model(actors_dir):
    """Train the KNN model on actor images"""
    print(f"Debug - Training model with directory: {actors_dir}")
    actor_features = []
    actor_names = []
    actor_images = []
    
    # Process all images in the Bollywood Actor Images directory and subdirectories
    for root, dirs, files in os.walk(actors_dir):
        print(f"Debug - Processing directory: {root}")
        for img_name in files:
            img_path = os.path.join(root, img_name)
            if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Extract actor name from directory name
                actor_name = os.path.basename(root)
                print(f"Debug - Processing image: {img_path} for actor: {actor_name}")
                features = extract_features(img_path)
                actor_features.append(features)
                actor_names.append(actor_name)
                # Store relative path from static directory
                rel_path = os.path.join('Bollywood Actor Images', os.path.basename(root), img_name)
                actor_images.append(rel_path)

    knn = NearestNeighbors(n_neighbors=1, metric='cosine')
    knn.fit(actor_features)
    
    return knn, actor_names, actor_images

def predict_similar_actor(user_image_path):
    """Predict the most similar actor for a given user image"""
    print(f"Debug - Predicting similar actor for image: {user_image_path}")
    # Load trained model and data
    knn, actor_names, actor_images = train_model('static/Bollywood Actor Images/')
    
    # Extract features from user image
    user_features = extract_features(user_image_path)
    
    # Find nearest neighbor
    _, indices = knn.kneighbors([user_features])
    actor_index = indices[0][0]
    
    # Convert path to use forward slashes and remove duplicate static prefix
    actor_image_path = actor_images[actor_index].replace('\\', '/')

    print(f"Debug - Actor image path: {actor_image_path}")
    return actor_names[actor_index], actor_image_path
