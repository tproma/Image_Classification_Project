import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename


    def predict(self):
        #load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))