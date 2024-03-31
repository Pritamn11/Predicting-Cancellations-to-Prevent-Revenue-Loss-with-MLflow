from src.utils.logger import logging
from src.utils.exception import CustomException
import sys
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
            
         

if __name__=="__main__":
    try:
        logging.info(f">>>>>>>>>>>>>>>>>> Stage --> {STAGE_NAME} <<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f"=======> Stage {STAGE_NAME} completed <======= \n\nx==========x")
    except Exception as e:
        logging.exception(f"Error in {STAGE_NAME} stage: {e}")
        raise CustomException(e,sys)
    