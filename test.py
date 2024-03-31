from src.utils.common import *
from pathlib import Path    
from src.utils.exception import CustomException
from src.utils.logger import logging
import sys

try:
    # Code that may raise an exception
    x = 1 / 1  # This will raise a ZeroDivisionError
    logging.info("This is test logging end")
except Exception as e:
    # Handle the specific exception (ZeroDivisionError in this case)
    raise CustomException(e,sys)