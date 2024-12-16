from flask import Flask
from flask_cors import CORS
from utils.ModelLoader import ModelLoader
from services.ModelService import ModelService
from services.PreprocessingService import PreprocessingService
from controllers.ImageController import ImageController
from controllers.MetricsController import MetricsController

app = Flask(__name__)
CORS(app)

model_paths = {
    "raw": "models/model_raw.pt",
    "bilateral": "models/model_bilateral.pt",
    "canny": "models/model_canny.pt"
}

from utils.ModelDefinition import get_model

model_loader = ModelLoader(model_paths, get_model)
model_service = ModelService(model_loader)
preprocessing_service = PreprocessingService()

ImageController(app, model_service, preprocessing_service)
MetricsController(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
