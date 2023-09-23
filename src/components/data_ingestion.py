import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import logger
from exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
path = 'logs\data_ingestion.txt'

logger(path,'data_ingestion.py file is started executing')
@dataclass

class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','data.csv')


class DataIngestion:
    
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
        
    def initial_data_ingestion(self):
        logger(path,'Data ingestion is started')
        try:
            df = pd.read_csv("E:\\Neoron\\Programming_Practice\\Machine_Learning_Project\\ml_Score_Prediction\\Data\\stud.csv")
            logger(path,'Data ingestion is completed')
            
            os.makedirs('artifacts',exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logger(path,'Raw data is saved in artifacts folder')
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            logger(path,'Train data is saved in artifacts folder')
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logger(path,'Test data is saved in artifacts folder')
            
            return(
                self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logger(path,'Error occured while reading the data')
            raise CustomException(e,sys)
        
        

'''if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data_ingestion.initial_data_ingestion()'''