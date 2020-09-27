# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:16:18 2020

@author: Asus
"""

#Import Library
import pandas as pd

#Membaca Dataset
dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/pythonTutorial/online_raw.csv')

# Checking for missing values per feature
print('\nMissing Values per Feature')
print(dataset.isnull().sum())

# Total missing values
print('\nTotal Missing Values')
print(dataset.isnull().sum().sum())

# Method [1] Drop rows with missing value   
dataset_clean = dataset.dropna()  
print('\nUkuran dataset_clean:', dataset_clean.shape) 

# Method [2] Impute missing value
print("Before imputation:")
## Checking missing value for each feature  
print(dataset.isnull().sum())
## Counting total missing value  
print(dataset.isnull().sum().sum())

print("\nAfter imputation:")
## Fill missing value with mean of feature value  
dataset.fillna(dataset.mean(), inplace = True)
## Checking missing value for each feature  
print(dataset.isnull().sum())
## Counting total missing value  
print(dataset.isnull().sum().sum())