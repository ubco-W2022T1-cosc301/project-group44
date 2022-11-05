# Matthew Enverga's Function 

import pandas as pd 

def load_and_process(rawData):
    
    df_clean = (pd.read_csv(rawData).drop(['children', 'sex'], axis=1).dropna(axis=0))
    
    df_clean['smoker'] = df_clean['smoker'].map({'yes': 1, 'no': 0})
    df_clean['bmi'] = df_clean['bmi'].round(decimals = 2)
    df_clean['charges'] = df_clean['charges'].round(decimals = 2)
    
    return df_clean