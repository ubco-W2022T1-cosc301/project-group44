#Isabella Mendoza's function

import pandas as pd

def load_and_process(rawData):
    
    #process data
    df1 = (
        pd.read_csv(rawData)
        .drop(['region','children', 'sex', ''], axis=1)
        .dropna(axis=0)
    )
    
    #alter representation of values
    df1['smoker'] = df1['smoker'].map({'yes': 1, 'no': 0})
    df1['bmi'] = df1['bmi'].round(decimals = 2)
    df1['charges'] = df1['charges'].round(decimals = 2)
    
    return df1