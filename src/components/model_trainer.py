import os
import sys
sys.path.append( os. path. dirname( os. path. dirname( os. path. abspath(__file__))))
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    AdaBoostRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

from exception import CustomException
from logger import logger
from utils import save_object,evaluate_models
path = 'E:\\Neoron\\Programming_Practice\\Machine_Learning_Project\\ml_Score_Prediction\\logs\\model_trainer.txt'
logger(path,'Importing all libraries')


@dataclass
class ModelTrainerConfig:
    train_model_file_path  = os.path.join("artifact","model.pkl")
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
        
    def initiate_model_trainer(self,train_array, test_array):
        
        try:
            logger(path, 'spliting train and test data')
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            logger(path, 'train and test data spliting is done')
            '''
            train_array[:,:-1] extracts all the columns from train_array except for the last one,
            which is assumed to be the labels. This is your training data.
            
            train_array[:,-1] extracts only the last column from train_array, 
            which is assumed to be the labels for the training data.
            
            test_array[:,:-1] extracts all the columns from test_array except 
            for the last one, which is assumed to be the labels.
            This is your testing data.
            
            test_array[:,-1] extracts only the last column from test_array, 
            which is assumed to be the labels for the testing data.
            
            '''
            logger(path, 'Model specification is started')
            model = {
                'LinearRegression': LinearRegression(),
                #'DecisionTreeRegressor': DecisionTreeRegressor(),
                #'RandomForestRegressor': RandomForestRegressor(),
                #'GradientBoostingRegressor': GradientBoostingRegressor(),
                #'AdaBoostRegressor': AdaBoostRegressor(),
                #'SVR': SVR(),
                'XGBRegressor': XGBRegressor(),
                #'CatBoostRegressor': CatBoostRegressor()
            }
            logger(path, 'Model specification is done')
            
            params={
                
                
                "LinearRegression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                }
                
            }
            
            model_report:dict = evaluate_models(X_train= X_train,
                                               y_train= y_train,
                                               X_test= X_test,
                                               y_test= y_test,
                                               models= model,
                                               param = params
                                               )
            
            
            # To get the best model score from dictionary
            best_model_score = max(sorted(model_report.values()))
            logger(path, 'To get the best model score from dictionary')
            
            # To get the best model name from dictionary
            logger(path, 'To get the best model name from dictionary')
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)]
            
            best_model = model[best_model_name]
            logger(path, 'best model is selected')
            
            logger(path, 'best model is trained')
            
            
            
            
            
            save_object(
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model
                )
            logger(path, 'Model is saved')    
                
            
            
            predicted = best_model.predict(X_test)
            logger(path, 'Model is predicted')
            
            r2 = r2_score(y_test,predicted)
            logger(path, 'R2 score is calculated')
            
            return r2
        
            
            
             
        except Exception as e:
            logger(path, 'Exception occured in initiate_model_trainer method of ModelTrainer class')
            raise CustomException(e,sys)
        
        
        
        
        
'''
                "DecisionTreeRegressor": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },

                "RandomForestRegressor":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "GradientBoostingRegressor":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoostRegressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoostRegressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "SVR":{
                    
                    'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
                    'C': [0.1, 1, 10],
                    'epsilon': [0.01, 0.1, 1],
                    'degree': [2, 3, 4],
                    'gamma': [0.1, 1, 'scale', 'auto']
                }

'''