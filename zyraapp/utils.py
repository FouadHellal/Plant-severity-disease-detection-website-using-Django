
from rembg import remove #utilisé pour la suppression de l'arrière-plan (background)
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
import os
import cv2
import numpy as np
import pandas as pd
from rembg import remove  
from fcmeans import FCM
from skimage.io import imread
from skimage.transform import resize

import cv2
import numpy as np
from skimage.transform import resize
import cv2
import numpy as np
from skimage.transform import resize
from PIL import Image

def load_and_prepare_image(image_path, target_size=(224, 224)):
    image = imread(image_path) / 255.0  # Charger et normaliser l'image
    image_resized = resize(image, target_size + (3,), preserve_range=True)  # Redimensionner l'image
    image_resized = np.expand_dims(image_resized, axis=0)  # Ajouter une dimension batch
    return image_resized

def create_mask(original_image, binarized_mask, alpha_mask):
    # Créer un masque vide
    new_mask = np.zeros_like(original_image)

    # Les pixels blancs de binarized_mask en rouge dans le plan rouge
    new_mask[binarized_mask[:,:,0] == 1, 0] = 255

    # Les pixels True de alpha_mask en vert dans le plan vert
    new_mask[alpha_mask & (binarized_mask[:,:,0] == 0), 1] = 255

    return new_mask

