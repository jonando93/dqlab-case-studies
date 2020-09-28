# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:05:12 2020

@author: jonando93
"""

#Import Library
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#Membaca Dataset
dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/pythonTutorial/online_raw.csv')
  
#Define MinMaxScaler as scaler  
scaler = MinMaxScaler()  

#list all the feature that need to be scaled  
scaling_column = ['Administrative','Administrative_Duration','Informational','Informational_Duration','ProductRelated','ProductRelated_Duration','BounceRates','ExitRates','PageValues']

#Apply fit_transfrom to scale selected feature  
dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])

#Cheking min and max value of the scaling_column
print(dataset[scaling_column].describe().T[['min','max']])
