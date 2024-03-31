from src.utils.logger import logging
from src.utils.exception import CustomException
import sys
from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from pathlib import Path
 

STAGE_NAME = 'Data Transformation stage'

class DataTransformationTrainingPipeline:

    def __init__(self):
        pass 

    
    def main(self):
        try :
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                preprocessor = data_transformation.get_data_transformer_object()
                train_path,test_path = data_transformation.train_test_split()
                train_arr, test_arr = data_transformation.initiate_data_transformation(train_path,test_path)
            else:
                raise Exception("You data schema is not valid")
    
        except Exception as e:
            raise CustomException(e,sys)




if __name__=="__main__":
    try:
        logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        logging.exception(f"Error in {STAGE_NAME} stage: {e}") 

