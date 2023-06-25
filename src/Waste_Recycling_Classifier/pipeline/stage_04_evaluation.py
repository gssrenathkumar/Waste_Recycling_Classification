from Waste_Recycling_Classifier.config.configuration import ConfigurationManager
from Waste_Recycling_Classifier.components.evaluation import Evaluation
from Waste_Recycling_Classifier import logger

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_evaluation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

