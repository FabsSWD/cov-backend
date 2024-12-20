import torch.nn as nn
from torchvision.models import resnet18


def get_model(num_classes):
    model = resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model
