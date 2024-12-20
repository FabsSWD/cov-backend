import numpy as np
from PIL import Image


class ImageUtils:
    @staticmethod
    def validate_image(image):
        if not isinstance(image, np.ndarray):
            raise ValueError("La imagen debe ser un arreglo numpy.")

    @staticmethod
    def normalize_image(image):
        return image / 255.0

    @staticmethod
    def convert_image_to_tensor(image):
        tensor = np.transpose(image, (2, 0, 1))  # Canales primero
        return tensor[np.newaxis, ...]
