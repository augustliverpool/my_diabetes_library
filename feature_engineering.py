# my_diabetes_library/feature_engineering.py
import pandas as pd
def create_dummies(data, column):

    return pd.get_dummies(data, columns=[column])

def create_binary_gender(data):
    data['gender'] = data['gender'].apply(lambda x: 1 if x == 'M' else 0)
    return data
