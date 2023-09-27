import os 
import sys
import pickle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.exception import CustomException
from src.logger import logger
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    
    
    def predict(self,feature):
        
        try:
            model_path = 'artifacts\\model.pkl'
            preprocessor_path = 'artifacts\\preprocessor.pkl'
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)
            data_scaled = preprocessor.transform(feature)
            prediction = model.predict(data_scaled)
            return prediction
        
        
        
        
        
        except Exception as e:
            raise CustomException(e,sys)
        
    
    
        
