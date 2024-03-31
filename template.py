import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format="%(asctime)s : %(lineno)d %(name)s - %(levelname)s - %(message)s")

# project_name = "MLproject"

# list_of_files = [
#     ".github/workflows/.gitkeep",
#     f"src/__init__.py",
#     f"src/components/__init__.py",
#     f"src/utils/__init__.py",
#     f"src/utils/common.py",
#     f"src/config/__init__.py",
#     f"src/config/configuration.py",
#     f"src/pipeline/__init__.py",
#     f"src/entity/__init__.py",
#     f"src/entity/config_entity.py",
#     f"src/constants/__init__.py",
#     "config/config.yaml",
#     "params.yaml",
#     "schema.yaml",
#     "main.py",
#     "app.py",
#     "Dockerfile",
#     "requirements.txt",
#     "setup.py",
#     "research/trials.ipynb",
#     "templates/index.html",
#     "test.py"
# ]



for file_path_str in list_of_files:
    file_path = Path(file_path_str)

    # Creating the directory
    os.makedirs(file_path.parent, exist_ok=True)
    logging.info(f"{file_path.parent} directory created")

    # Creating an empty file if its not a directory
    if not file_path.is_dir():
        file_path.touch()
        logging.info(f"{file_path} file created")
    

# Verifying the directory structure and files using os.walk
for root, dirs, files in os.walk('.'):
    logging.info(f"Current directory: {root}")
    logging.info(f"Subdirectories: {dirs}")
    logging.info(f"Files: {files}")
    logging.info("")
