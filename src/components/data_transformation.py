import os 
import sys
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import logger
from exception import CustomException
from utils import save_object



path_tran = 'E:\\Neoron\\Programming_Practice\\Machine_Learning_Project\\ml_Score_Prediction\\logs\\data_transformation.txt'

logger(path_tran,'Importing all libraries')

class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')
    
    logger(path_tran,'DataTransformationConfig class started')
class DataTransformation:
    
    def __init__(self):
        self.Data_transformation_config = DataTransformationConfig()
        
    logger(path_tran,'DataTransformation class started')
    def get_data_transformar_obj(self):
        try:
            numerical_features = ['writing_score','reading_score']
            categorical_features = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]
            logger(path_tran, 'Numerical and categorical features are defined')
            
            num_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy="median")),
                ('scaler', StandardScaler())
            ])
            logger(path_tran, 'num_pipeline is defined')
            
            
            cat_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy="most_frequent")),
                ('one_hot_encoder', OneHotEncoder()),
                ('scaler', StandardScaler(with_mean=False))
            ])
            logger(path_tran, 'cat_pipeline is defined')
            
            
            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_features),
                ('cat_pipeline', cat_pipeline, categorical_features)
            ])
            logger(path_tran, 'Column transformation is defined')
            
            logger(path_tran, 'DataTransformation class ended')
            return preprocessor
        
        
        
        except Exception as e:
            logger(path_tran, 'Exception occured in get_data_transformar_obj method of DataTransformation class')
            raise CustomException(e,sys)
        
    
    
    
    def initiate_data_transformation(self,train_data_path,test_data_path):
        logger(path_tran, 'initiate_data_transformation method of DataTransformation class started')
        try:
            
            train_df = pd.read_csv(train_data_path)
            logger(path_tran, 'Train data is read')
            test_df = pd.read_csv(test_data_path)
            logger(path_tran, 'Test data is read')
            
            
            preprocessing_obj = self.get_data_transformar_obj()
            logger(path_tran, 'preprocessing_obj is called')
            
            target_column_name = 'math_score'
            logger(path_tran, 'Target column is defined')
            
            numerical_column = ['writing_score','reading_score']
            logger(path_tran, 'Numerical column is defined')
            
            input_feature_train = train_df.drop(target_column_name,axis=1)
            terget_feature_train = train_df[target_column_name]
            logger(path_tran, 'Input and target features are defined for train data')
            
            input_feature_test = test_df.drop(target_column_name,axis=1)
            terget_feature_test = test_df[target_column_name]
            logger(path_tran, 'Input and target features are defined for test data')
            
            
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train)
            logger(path_tran, 'Input feature train data is transformed')
            
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test)
            logger(path_tran, 'Input feature test data is transformed')
            
            
            
            train_arr = np.c_[input_feature_train_arr,
                              np.array(terget_feature_train)]
            logger(path_tran, 'Train data is concatenated')
            
            
            test_arr = np.c_[input_feature_test_arr,
                             np.array(terget_feature_test)]
            logger(path_tran, 'Test data is concatenated')
            
            
            save_object (
                file_path = self.Data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            logger(path_tran , 'save_object function is called')
            
            return (
                train_arr,
                test_arr,
                self.Data_transformation_config.preprocessor_obj_file_path
            )
            
            
        except Exception as e:
            logger(path_tran, 'Exception occured while executing initiate_data_transformation method of DataTransformation class')
            raise CustomException(e,sys)
            


if __name__ == "__main__":
    a = DataTransformation()
    a.initiate_data_transformation('E:\\Neoron\\Programming_Practice\\Machine_Learning_Project\\ml_Score_Prediction\\artifacts\\train.csv','E:\\Neoron\\Programming_Practice\\Machine_Learning_Project\\ml_Score_Prediction\\artifacts\\test.csv')