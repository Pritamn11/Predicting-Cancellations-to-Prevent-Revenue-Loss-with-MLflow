from src.utils.logger import logging
from src.utils.exception import CustomException
import sys
from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation 

STAGE_NAME = "Model Evaluation stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    try:
        logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        logging.exception(f"Error in {STAGE_NAME} stage: {e}")
