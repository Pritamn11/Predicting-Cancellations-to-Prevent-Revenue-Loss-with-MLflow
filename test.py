from src.utils.common import *
from pathlib import Path    
from src.utils.exception import CustomException
from src.utils.logger import logging
import sys

try:
    logging.info("This is test logging initiate")
    x = 1 / 1  
    logging.info("This is test logging end")
except Exception as e:
    raise CustomException(e,sys)