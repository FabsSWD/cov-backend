import torch

class ModelLoader:
    def __init__(self, model_paths, model_class):
        self.models = {}
        self.model_class = model_class
        for name, path in model_paths.items():
            self.models[name] = self.load_model(path)

    def load_model(self, path):
        model = self.model_class(num_classes=3)
        model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
        model.eval()
        return model

    def get_model(self, model_name):
        if model_name in self.models:
            return self.models[model_name]
        else:
            raise ValueError(f"Modelo '{model_name}' no encontrado.")
