from src.data_ingestion import DataIngestion
from src.model_training import ModelTraining    
from config.paths_config import *
from src.data_preprocessing import DataProcessor
from utils.common_functions import read_yaml

if __name__=='__main__':

    config = read_yaml(CONFIG_PATH)

    data_ingestion = DataIngestion(config)
    data_ingestion.run()

    processor = DataProcessor(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)

    processor.process()