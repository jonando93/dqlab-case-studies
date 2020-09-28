# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:20:35 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#Membaca Dataset
dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/pythonTutorial/online_raw.csv')

# [1] DATA EXPLORATION
## Checking Data Dimension for Data Exploration
print('Shape dataset:', dataset.shape)
print('\nLima data teratas:\n', dataset.head())
print('\nInformasi dataset:')
print(dataset.info())
print('\nStatistik deskriptif:\n', dataset.describe())

## Checking Feature Correlation
dataset_corr = dataset.corr()
print('Korelasi dataset:\n', dataset.corr())
print('Distribusi Label (Revenue):\n', dataset['Revenue'].value_counts())

## Checking Feature Correlation using .loc
print('\nKorelasi BounceRates-ExitRates:', dataset_corr.loc['BounceRates', 'ExitRates'])
print('\nKorelasi Revenue-PageValues:', dataset_corr.loc['Revenue', 'PageValues'])
print('\nKorelasi TrafficType-Weekend:', dataset_corr.loc['TrafficType', 'Weekend'])

## Checking the Distribution of customers on Revenue
plt.rcParams['figure.figsize'] = (12,5)
plt.subplot(1, 2, 1)
sns.countplot(dataset['Revenue'], palette = 'pastel')
plt.title('Buy or Not', fontsize = 20)
plt.xlabel('Revenue or not', fontsize = 14)
plt.ylabel('count', fontsize = 14)

## Checking the Distribution of customers on Weekend
plt.subplot(1, 2, 2)
sns.countplot(dataset['Weekend'], palette = 'inferno')
plt.title('Purchase on Weekends', fontsize = 20)
plt.xlabel('Weekend or not', fontsize = 14)
plt.ylabel('count', fontsize = 14)
plt.show()

## Visualizing the distribution of customers around the Region
plt.hist(dataset['Region'], color = 'lightblue')
plt.title('Distribution of Customers', fontsize = 20)
plt.xlabel('Region Codes', fontsize = 14)
plt.ylabel('Count Users', fontsize = 14)
plt.show()

# [2] DATA PRE-PROCESSING - HANDLING MISSING VALUE
## Checking for missing values per feature
print('\nMissing Values per Feature')
print(dataset.isnull().sum())

## Total missing values
print('\nTotal Missing Values')
print(dataset.isnull().sum().sum())

## Method [1] Drop rows with missing value   
dataset_clean = dataset.dropna()  
print('\nUkuran dataset_clean:', dataset_clean.shape) 

## Method [2] Impute missing value using mean(), median(), etc.
print("Before imputation:")
### Checking missing value for each feature  
print(dataset.isnull().sum())
### Counting total missing value  
print(dataset.isnull().sum().sum())

print("\nAfter imputation:")
### Fill missing value with mean of feature value  
dataset.fillna(dataset.mean(), inplace = True)
### Checking missing value for each feature  
print(dataset.isnull().sum())
### Counting total missing value  
print(dataset.isnull().sum().sum())

# [3] DATA PRE-PROCESSING - DATA SCALING, STRING TO NUMERIC CONVERSION
## Define MinMaxScaler as scaler  
scaler = MinMaxScaler()  

## [Numeric Features] List all the feature that need to be scaled 
scaling_column = ['Administrative','Administrative_Duration','Informational','Informational_Duration','ProductRelated','ProductRelated_Duration','BounceRates','ExitRates','PageValues']

### Apply fit_transfrom to scale selected feature  
dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])

### Cheking min and max value of the scaling_column
print(dataset[scaling_column].describe().T[['min','max']])

print('')

## [String Features] String conversion to numeric
### Convert feature/column 'Month'
LE = LabelEncoder()
dataset['Month'] = LE.fit_transform(dataset['Month'])
print(LE.classes_)
print(np.sort(dataset['Month'].unique()))
print('')

### Convert feature/column 'VisitorType'
LE = LabelEncoder()
dataset['VisitorType'] = LE.fit_transform(dataset['VisitorType'])
print(LE.classes_)
print(np.sort(dataset['VisitorType'].unique()))
print('')

# [4] FEATURES & LABEL
## Removing the target column Revenue from dataset and assigning to X (FEATURE)
X = dataset.drop(['Revenue'], axis = 1)

## Assigning the target column Revenue to y (LABEL/TARGET)
y = dataset['Revenue']

## Checking the shapes
print('Shape of X:', X.shape)
print('Shape of y:', y.shape)

# [5] TRAINING & TEST DATASET
## Splitting the X, and y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

## Checking the shapes
print("Shape of X_train :", X_train.shape)
print("Shape of y_train :", y_train.shape)
print("Shape of X_test :", X_test.shape)
print("Shape of y_test :", y_test.shape)

# [6.1] TRAINING MODEL: FIT
## Call the classifier
model = DecisionTreeClassifier()
## Fit the classifier to the training data
model = model.fit(X_train,y_train)

# [6.2] TRAINING MODEL: PREDICT
## Apply the classifier/model to the test data
y_pred = model.predict(X_test)
print(y_pred.shape)