import pandas as pd
def remove_nan(data, columns):
    """删除指定列中包含NaN的行"""
    return data.dropna(subset=columns)

def fill_missing_values(data, columns):
    
    for column in columns:
        data[column].fillna(data[column].mean(), inplace=True)
    return data
