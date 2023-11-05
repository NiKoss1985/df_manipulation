#import libraries 
import pandas as pd
import numpy as np 

#upload .csv file in pandas 
dataframe = pd.read_csv(r'github.com/NiKoss1985/df_manipulation/blob/main/db/sales.csv')

#visualise top 5 rows to get an understanding of the DF and names of columns
dataframe.head()

#visualise dtypes to get an understanding of the DF
dataframe.dtypes

#use .info to find potential NaN values in the DF
dataframe.info()

