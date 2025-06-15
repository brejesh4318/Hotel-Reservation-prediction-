import os
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"file is not in the given path")
        with open(file_path,"r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("successfully read the yaml file")
            return config
        
    except Exception as e:
        logger.error("error while reading yaml file")
        raise CustomException("failed to read yaml file",e)

def load_data(path):
    try:
        logger.info("Loading Load")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"error loading the data {e}")
        raise CustomException("error loading data",e)