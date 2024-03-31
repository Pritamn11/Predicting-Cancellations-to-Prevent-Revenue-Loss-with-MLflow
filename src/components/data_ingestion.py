import os
import urllib.request as request
import zipfile
from src.utils.logger import logging
from src.utils.exception import CustomException
from src.utils.common import *
import sys
from src.entity.config_entity import DataIngestionConfig
                                      



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            source_url = self.config.source_URL
            file_id = source_url.split('/')[-2]
            filename, headers = request.urlretrieve(
                url = f"https://drive.google.com/uc?id={file_id}", 
                filename = self.config.local_data_file
            )
            logging.info(f"{filename} download with following info: \n {headers}")
        else:
            logging.info(f"File already exists of size : {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        """
        Extracts the zip file into the directory specified in the configuration.
        Functions returns None.
        """  
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_f:
            zip_f.extractall(unzip_path) 

