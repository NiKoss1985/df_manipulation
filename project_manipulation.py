# Import libraries 
import pandas as pd
import numpy as np 

# GitHub raw URL for the CSV file
csv_raw_url = 'https://raw.githubusercontent.com/NiKoss1985/df_manipulation/main/db/sales.csv'

# Upload .csv file in pandas 
dataframe = pd.read_csv(csv_raw_url)

# Visualise top 5 rows to get an understanding of the DF and names of columns
dataframe.head()

# Visualise dtypes to get an understanding of the DF
dataframe.dtypes

# Use .info to find potential NaN values in the DF
dataframe.info()


