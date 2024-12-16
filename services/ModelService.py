import torch

class ModelService:
    def __init__(self, model_loader):
        self.model_loader = model_loader

    def predict(self, model_name, input_tensor):
        model = self.model_loader.get_model(model_name)
        with torch.no_grad():
            output = model(input_tensor)
        return torch.argmax(output, dim=1).item()
