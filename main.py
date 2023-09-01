from ImageClassifier import logger
from ImageClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ImageClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from ImageClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from ImageClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Evaluation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


