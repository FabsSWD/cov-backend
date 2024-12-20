from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import io
import base64
import torch


class ImageController:
    def __init__(self, app, model_service, preprocessing_service):
        self.app = app
        self.model_service = model_service
        self.preprocessing_service = preprocessing_service
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/predict', methods=['POST'])
        def predict():
            if 'image' not in request.files or 'method' not in request.form or 'model' not in request.form:
                return jsonify({"error": "Faltan parámetros"}), 400

            image_file = request.files['image']
            method = request.form['method']
            model_name = request.form['model']

            try:
                image = Image.open(image_file).convert('RGB')
                image_array = np.array(image)

                preprocessed_image = self.preprocessing_service.preprocess_image(image_array, method)

                processed_image = Image.fromarray(preprocessed_image.astype(np.uint8))
                img_io = io.BytesIO()
                processed_image.save(img_io, format='PNG')
                img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

                input_tensor = torch.tensor(preprocessed_image, dtype=torch.float32).permute(2, 0, 1).unsqueeze(0)
                prediction = self.model_service.predict(model_name, input_tensor)

                if prediction is None:
                    raise ValueError("El modelo no devolvió una predicción válida.")

                return jsonify({
                    "prediction": prediction,
                    "processed_image": f"data:image/png;base64,{img_base64}"
                })

            except Exception as e:
                return jsonify({"error": str(e)}), 500
