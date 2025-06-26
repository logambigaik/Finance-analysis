import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import codecademylib3_seaborn
files = glob.glob('states*.csv')
census = []
for filename in files:
    census.append(pd.read_csv(filename))
[print(df.columns) for df in census]
[print(df.dtypes) for df in census]
[print(df.head()) for df in census]
for us_census in census:
  us_census['Income'] = us_census['Income'].str.replace(r'\$', '', regex=True)
  gender_split = us_census['GenderPop'].str.split('_', expand=True)
  print(gender_split)

  # Assign the split values to new columns
  # us_census['Men']= gender_split[0].str.replace('(\d+)','',regex=True).str.strip()
  # us_census['Women'] = gender_split[1].str.replace('(\d+)','',regex=True).str.strip()
  # print(us_census['Men'],us_census['Women'])
  us_census['Men']= gender_split[0].str.replace('M','',regex=True)
  us_census['Women']= gender_split[1].str.replace('F','',regex=True)
  print(us_census['Men'],us_census['Women'])

  us_census['Men'] =pd.to_numeric(us_census['Men'])
  us_census['Women'] =pd.to_numeric(us_census['Women'])
  print(us_census['Men'].dtypes,us_census['Women'].dtypes)
  
  us_census['Men'].fillna(0)
  us_census['Women'].fillna(0)
  us_census['Women'] = us_census['TotalPop']-us_census['Men']
  print(us_census.head(2))
  duplicates = us_census.duplicated()
  us_census.drop_duplicates()
  plt.scatter(us_census['Women'],us_census['Men'])
  plt.show()
  us_census = us_census.drop(labels='Unnamed: 0', axis=1)
  print(us_census.columns)
