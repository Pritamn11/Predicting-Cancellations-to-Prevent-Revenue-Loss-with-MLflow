import os 
from pathlib import Path
from typing import Any 
import yaml
from box.exceptions import BoxValueError 
from src.utils.logger import logging 
from src.utils.exception import CustomException
import json
import joblib 
from box import ConfigBox
from ensure import ensure_annotations
import sys



@ensure_annotations
def read_yaml(yaml_filepath: Path) -> ConfigBox:
    '''Reads a YAML file and returns a ConfigBox.
    Args:
        yaml_filepath (Path) : path of yaml file.
    Raises:
        ValueError : if YAML file is empty.
        yaml.YAMLError: If a YAML parsing error occurs.
        CustomException : If an error occurs while reading the YAML file.
    Returns:
        ConfigBox: A ConfigBox instance containing the YAML content.
    '''
    try:
        with open(yaml_filepath) as yaml_file:
            load_data = yaml.safe_load(yaml_file)
            logging.info(f"{yaml_filepath} yaml file loaded successfully")
            return ConfigBox(load_data)
    except BoxValueError:
        raise ValueError("yaml file is empty")  
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file '{yaml_filepath}': {e}")
    except Exception as e:
        raise CustomException(e,sys)
    


@ensure_annotations
def create_directories(directory_path: list, verbose=True):
    '''Create list of directories.
       Args:
           directory_path (list) : List of paths of directory.
           verbose : If True print log messages. Defaults to True.
    '''
    for path in directory_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at : {path}")

    
@ensure_annotations
def save_json(path_tosave:Path, data:dict):
    '''Saves data as JSON to the specified file path.
    Args:
        path_tosave (Path): The file path where the JSON data will be saved.
        data (dict): The dictionary containing the data to be saved as JSON.

    Example:
        save_json(path_tosave=Path("data.json"),data={"key": "value"})
    '''
    with open(path_tosave,"w") as save_file:
        json.dump(data,save_file,indent=4)
    logging.info(f"JSON file saved at {path_tosave}")


@ensure_annotations
def load_json(json_filepath: Path) -> ConfigBox:
    '''Load JSON file data.
    Args:
        json_filepath (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    '''
    try:
        with open(json_filepath) as file:
            load_data = json.load(file)
        logging.info(f"JSON file loaded successfully from : {json_filepath}")
        return ConfigBox(load_data) 
    except Exception as e:
        raise CustomException(e,sys)
    

@ensure_annotations
def save_binary(binary_data:Any, path_tosave:Path):
    '''Save binary data to a file
    Args:
        binary_data (Any) : The binary data to be saved to the file.. 
        path_tosave (Path) : The file path where the binary data will be saved.
    '''
    joblib.dump(value=binary_data, filename=path_tosave)
    logging.info(f"Binary  file saved at path {path_tosave}")


@ensure_annotations
def load_binary(binary_filepath:Path) -> Any:
    '''Load data from a binary file.
    Args:
        binary_filepath (Path) : Path of binary file.
    Returns:
        Any: Object stored in the binary file..
    '''
    data = joblib.load(binary_filepath)
    logging.info(f"Binary file loaded from {binary_filepath}")
    return data
    


@ensure_annotations
def get_size(filepath:Path) -> int:
    '''Get the size of a file in kilobytes.
    Args:
        filepath (Path) : Path of the file.
    Return:
        int : Size of the file in kilobytes.    
    ''' 
    try:
        file_size = round(os.path.getsize(filepath) / 1024)
        return f"{file_size}KB"
    except Exception as e:
        raise CustomException(e,sys)



