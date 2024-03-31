from src.utils.logger import logging
from src.utils.exception import CustomException
import sys
from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer


STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:

    def __init__(self):
        pass 

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train() 
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    try:
        logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        logging.exception(f"Error in {STAGE_NAME} stage: {e}") 
