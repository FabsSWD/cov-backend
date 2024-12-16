import cv2
import numpy as np

class PreprocessingService:
    def apply_bilateral_filter(self, image):
        return cv2.bilateralFilter(image, 9, 75, 75)

    def apply_canny_edge(self, image):
        image_uint8 = image.astype(np.uint8)
        edges = cv2.Canny(image_uint8, 100, 200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    def preprocess_image(self, image, method):
        if method == "bilateral":
            return self.apply_bilateral_filter(image)
        elif method == "canny":
            return self.apply_canny_edge(image)
        elif method == "raw":
            if len(image.shape) == 2:
                return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            return image
        else:
            raise ValueError("Método de preprocesamiento no soportado.")
