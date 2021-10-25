import pandas as pd
import numpy as np

def null_count(df):
    '''Returns the number of null values 
    across the entire dataframe'''
    return df.isnull().sum().sum()

# print(null_count(pd.DataFrame({'a': [1,2,np.NaN], 'b':[np.NaN, np.NaN, 6]})))