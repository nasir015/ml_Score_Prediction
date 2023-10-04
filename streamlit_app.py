import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.exception import CustomException
from src.logger import logger
from src.utils import load_object



st.title('''Mathematics Score Prediction App''')

def user_input_features():
    
    gender = st.selectbox('Gender',('female', 'male'))
    race_ethnicity = st.selectbox('Race Ethnicity',('group B' ,'group C', 'group A' ,'group D', 'group E'))
    parental_level_of_education = st.selectbox('Parental Level of Education',("bachelor's degree" ,
                                                                                    'some college' ,
                                                                                    "master's degree",
                                                                                    "associate's degree",
                                                                                    'high school' ,
                                                                                    'some high school'))
    lunch = st.selectbox('lunch',('standard' ,'free/reduced'))
    test_preparation_course = st.selectbox('Test Preparation Course',('none' ,'completed'))
    writing_score = st.number_input('Writing Score')
    reading_score = st.number_input('Reading Score')
    data = {'gender': gender,
            'race_ethnicity': race_ethnicity,
            'parental_level_of_education': parental_level_of_education,
            'lunch': lunch,
            'test_preparation_course': test_preparation_course,
            'writing_score': writing_score,
            'reading_score': reading_score}

    features = pd.DataFrame(data, index=[0])
    return features
        
input_df = user_input_features()








if st.button('Recommend'):
    def predict(feature):
            
        try:
            model_path = 'artifact\\model.pkl'
            preprocessor_path = 'artifacts\\preprocessor.pkl'
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)
            data_scaled = preprocessor.transform(feature)
            prediction = model.predict(data_scaled)
            return prediction
            
        except Exception as e:
            raise CustomException(e,sys)
        
    prediction = predict(input_df)

    st.write( 'Math score is: ',prediction[0])