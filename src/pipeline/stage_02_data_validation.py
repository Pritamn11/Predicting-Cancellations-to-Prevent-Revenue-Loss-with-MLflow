from src.utils.logger import logging
from src.utils.exception import CustomException
import sys
from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation 


STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__=="__main__":
    try:
        logging.info(f">>>>>>>>>>>>>>>>>> Stage --> {STAGE_NAME} <<<<<<<<<<<<<<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
            logging.exception(f"Error in {STAGE_NAME} stage: {e}")
            raise CustomException(e,sys)
    