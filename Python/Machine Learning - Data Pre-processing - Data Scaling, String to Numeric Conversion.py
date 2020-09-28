# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:05:12 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder

#Membaca Dataset
dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/pythonTutorial/online_raw.csv')
  
#Define MinMaxScaler as scaler  
scaler = MinMaxScaler()  

#[Numeric Features] List all the feature that need to be scaled 
scaling_column = ['Administrative','Administrative_Duration','Informational','Informational_Duration','ProductRelated','ProductRelated_Duration','BounceRates','ExitRates','PageValues']

##Apply fit_transfrom to scale selected feature  
dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])

##Cheking min and max value of the scaling_column
print(dataset[scaling_column].describe().T[['min','max']])

print('')

#[String Features] String conversion to numeric
## Convert feature/column 'Month'
LE = LabelEncoder()
dataset['Month'] = LE.fit_transform(dataset['Month'])
print(LE.classes_)
print(np.sort(dataset['Month'].unique()))
print('')

## Convert feature/column 'VisitorType'
LE = LabelEncoder()
dataset['VisitorType'] = LE.fit_transform(dataset['VisitorType'])
print(LE.classes_)
print(np.sort(dataset['VisitorType'].unique()))