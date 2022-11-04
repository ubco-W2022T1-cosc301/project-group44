import pandas as pd

def load_and_process(dfRaw):
    df = pd.read_csv(dfRaw)
    dfClean = (df.copy()
                  .drop(['bmi', 'children','smoker', 'region'], axis=1)
                  .dropna(axis=0)
                 )
    dfClean['charges'] = dfClean['charges'].round(decimals = 2)
    
    
    return dfClean