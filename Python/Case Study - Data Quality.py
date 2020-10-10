# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:26:20 2020

@author: jonando93
"""

# Import Library
import pandas as pd
import matplotlib.pyplot as plt

# Membaca Dataset
uncleaned_raw = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/uncleaned_raw.csv')

# Inspeksi dataframe uncleaned_raw
print('Lima data teratas:') 
print(uncleaned_raw.head())

# Check kolom yang mengandung missing value
print('\nKolom dengan missing value:') 
print(uncleaned_raw.isnull().any())

# Persentase missing value
length_qty = len(uncleaned_raw['Quantity'])
count_qty = uncleaned_raw['Quantity'].count()

# Mengurangi length dengan count
number_of_missing_values_qty = length_qty - count_qty

# Mengubah ke bentuk float
float_of_missing_values_qty = float(number_of_missing_values_qty / length_qty) 

# Mengubah ke dalam bentuk persen
pct_of_missing_values_qty = '{0:.1f}%'.format(float_of_missing_values_qty * 100) 

# Print hasil percent dari missing value
print('\nPersentase missing value kolom Quantity:', pct_of_missing_values_qty)

# Mengisi missing value tersebut dengan mean dari kolom tersebut
uncleaned_raw['Quantity'] = uncleaned_raw['Quantity'].fillna(uncleaned_raw['Quantity'].mean())

# Mengetahui kolom yang memiliki outliers!
uncleaned_raw.boxplot()
plt.show()

# Check IQR
Q1 = uncleaned_raw['UnitPrice'].quantile(0.25)
Q3 = uncleaned_raw['UnitPrice'].quantile(0.75)
IQR = Q3 - Q1

# Removing outliers
uncleaned_raw = uncleaned_raw[~((uncleaned_raw[['UnitPrice']] < (Q1 - 1.5 * IQR)) | (uncleaned_raw[['UnitPrice']] > (Q3 + 1.5 * IQR)))]

# Check for duplication
print(uncleaned_raw.duplicated(subset=None))

# Remove duplication
uncleaned_raw = uncleaned_raw.drop_duplicates()