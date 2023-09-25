import os 
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd
import dill
from logger import logger
from exception import CustomException
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from exception import CustomException
path_utils = "E:\\Neoron\\Programming_Practice\\Machine_Learning_Project\\ml_Score_Prediction\\logs\\utils.txt"


logger(path_utils,'save_object function is started')
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    logger(path_utils,'save_object function is completed')


logger(path_utils,'evaluate_models function is started')
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
            logger(path_utils,'evaluate_models function is completed')

        return report
    

    except Exception as e:
        raise CustomException(e, sys)
    
logger(path_utils,'load_object function is started')   
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
        

    except Exception as e:
        raise CustomException(e, sys)
logger(path_utils,'load_object function is completed')