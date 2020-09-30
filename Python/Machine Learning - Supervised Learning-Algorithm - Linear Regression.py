# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:39:52 2020

@author: jonando93
"""

# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Membaca Dataset
housing = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/pythonTutorial/housing_boston.csv')

# [1] DATA EXPLORATION
## Checking Data Dimension for Data Exploration
print('Shape dataset:', housing.shape)
print('\nLima data teratas:\n', housing.head())
print('\nInformasi dataset:')
print(housing.info())
print('\nStatistik deskriptif:\n', housing.describe())

## Checking Feature Correlation
housing_corr = housing.corr()
print('\nKorelasi dataset:\n', housing.corr())

# [2] DATA PRE-PROCESSING - DATA SCALING
## Data Rescaling
data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
housing[['RM','LSTAT','PTRATIO','MEDV']] = data_scaler.fit_transform(housing[['RM','LSTAT','PTRATIO','MEDV']])

### Cheking min and max value of the scaling_column
print('')
print(housing[['RM','LSTAT','PTRATIO','MEDV']].describe().T[['min','max']])

# [3] FEATURES & LABEL
## Getting dependent and independent variables
X = housing.drop(['MEDV'], axis = 1) #Feature
y = housing['MEDV'] #Label

## Checking the shapes
print('\nShape of X:', X.shape)
print('Shape of y:', y.shape)

# [4] TRAINING & TEST DATASET
## splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

## checking the shapes  
print('\nShape of X_train :', X_train.shape)
print('Shape of y_train :', y_train.shape)
print('Shape of X_test :', X_test.shape)
print('Shape of y_test :', y_test.shape)

# [5.1] TRAINING MODEL: FIT - LINEAR REGRESSION 
## Call the regressor
reg = LinearRegression()
## Fit the regressor to the training data  
reg = reg.fit(X_train,y_train)

# [5.2] TRAINING MODEL: PREDICT - LINEAR REGRESSION
## Apply the regressor/model to the test data  
y_pred = reg.predict(X_test)

# [6] EVALUATE MODEL PERFORMANCE - LINEAR REGRESSION
## Calculating MSE, lower the value better it is. 0 means perfect prediction
mse = mean_squared_error(y_test, y_pred)
print('\nMean squared error of testing set:', mse)
## Calculating MAE
mae = mean_absolute_error(y_test, y_pred)
print('Mean absolute error of testing set:', mae)
## Calculating RMSE
rmse = np.sqrt(mse)
print('Root Mean Squared Error of testing set:', rmse)

# [7] PLOTTING MODEL
## Plotting y_test dan y_pred
plt.scatter(y_test, y_pred, c = 'green')
plt.xlabel('Price Actual')
plt.ylabel('Predicted value')
plt.title('True value vs predicted value : Linear Regression')
plt.show()