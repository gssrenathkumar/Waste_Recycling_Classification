from Waste_Recycling_Classifier.config.configuration import ConfigurationManager
from Waste_Recycling_Classifier.components.prepare_base_model import PrepareBaseModel
from Waste_Recycling_Classifier import logger
from Waste_Recycling_Classifier import logger


STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


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