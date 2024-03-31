import os
import sys
from src.utils.logger import logging
from src.utils.exception import CustomException
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
 

STAGE_NAME = "Data Ingestion"
if __name__=="__main__":
    try:
        logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        raise CustomException(e,sys)    



STAGE_NAME = "Data Validation stage"
if __name__=="__main__":
    try:
        logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        raise CustomException(e,sys)    
    

STAGE_NAME = "Data Transformation stage"
if __name__=="__main__":
    try:
        logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        raise CustomException(e,sys) 


STAGE_NAME = "Model Trainer stage"
if __name__=="__main__":
    try:
        logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
        model_trainer = ModelTrainerTrainingPipeline()
        model_trainer.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        raise CustomException(e,sys)    
    

