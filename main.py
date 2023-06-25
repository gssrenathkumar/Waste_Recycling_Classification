from Waste_Recycling_Classifier import logger
from Waste_Recycling_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Waste_Recycling_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

logger.info("Welcome to our custom logging")

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Preparation of Base Model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>>>>>>>>>>>Stage: {STAGE_NAME} Started Successfully")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>Stage: {STAGE_NAME} Completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e