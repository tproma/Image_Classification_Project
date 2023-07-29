import os
import urllib.request as request
import zipfile
from ImageClassifier import logger
from ImageClassifier.utils.common import get_size
from ImageClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

