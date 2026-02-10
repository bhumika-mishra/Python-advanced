import pandas as pd
import numpy as np 

exam_data = {'Name':['Ram','Pragati','Ananya','Arnav','Anusaya','Srittam','Devika','Janvi','Suhani','Ayush'],'Score':[10,9,7,12,np.nan,20,14,np.nan,6,10], 'Attempts':[1,2,1,1,1,3,4,1,1,2],'Qualify':['Yes','No','No','Yes','No','Yes','Yes','No','No','Yes']}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data, index = labels)
print("Summary : ")
print(df.info())
print(df.head())
print(df.tail())
print(df.isnull().sum())
df.fillna(1,inplace=True)
print(df.head(10))
df1 = pd.read_csv('gender_submission.csv')
print(df1.head())
