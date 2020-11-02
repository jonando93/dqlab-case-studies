# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:35:16 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import numpy as np
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

#Membaca Dataset
df = pd.read_excel("https://academy.dqlab.id/dataset/credit_scoring_dqlab.xlsx", index_col=0)

#Quick glimpse at the Dataset
print(df.head())
print(df.info())
print(df.describe())
print(df.describe(include=['object']))

#Convert risk_rating datatype from int64 to object
df['risk_rating'] = df['risk_rating'].astype(object)
print('\n', df['risk_rating'].dtypes) #verifying

#Membuat variable baru untuk variable input dari dataset
datafeed = df[['durasi_pinjaman_bulan', 'jumlah_tanggungan']]
print('\n', datafeed.dtypes)

population = list(range(1,900))

#Membuat training set dan testing set
#Training Set - dataset yang akan digunakan oleh algoritma untuk dianalisa.
#Testing Set - dataset yang tidak digunakan oleh algoritma, tetapi untuk menguji model yang dibentuk dari training set.
X_data = datafeed
Y_data = df[['risk_rating']].astype(int)

#create random train/test split
indices = range(X_data.shape[0])
num_training_instances = int(8/9 * X_data.shape[0])
random.shuffle(list(indices))
train_indices = indices[:num_training_instances]
test_indices = indices[num_training_instances:]

#Split the actual data
X_data_train, X_data_test = X_data.iloc[train_indices], X_data.iloc[test_indices]
Y_data_train, Y_data_test = Y_data.iloc[train_indices], Y_data.iloc[test_indices]

print('Shape of X_data_train : ',X_data_train.shape)
print('Shape of X_data_test : ',X_data_test.shape)
print('Shape of Y_data_train : ',Y_data_train.shape)
print('Shape of Y_data_test : ',Y_data_test.shape)

#Menghasilkan Model Decision Class Tree
#TRAINING MODEL: FIT - DECISION TREE CLASSIFIER
##Call the classifier
model = DecisionTreeClassifier()
##Fit the classifier to the training data
model = model.fit(X_data_train, Y_data_train)

#TRAINING MODEL: PREDICT
##Apply the classifier/model to the test data
y_pred = model.predict(X_data_test)
print(y_pred.shape)

#EVALUATING MODEL PERFORMANCE - DECISION TREE CLASSIFIER
## Evaluating the model
print('\nTraining Accuracy :', model.score(X_data_train, Y_data_train))
print('Testing Accuracy :', model.score(X_data_test, Y_data_test))

## Confusion matrix
print('\nConfusion matrix:')
cm = confusion_matrix(Y_data_test, y_pred)
print(cm)

## Classification report
print('\nClassification report:')
cr = classification_report(Y_data_test, y_pred)
print(cr)

#Implementing Machine Learning Model to dataframe
y_pred1 = model.predict(datafeed)

#Adding new column to record Model Prediction
df['risk_rating_prediction'] = y_pred1
print(df['risk_rating_prediction'].shape)

