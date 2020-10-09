# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:26:46 2020

@author: jonando93
"""

#Import Library
import pandas as pd

#Membaca Dataset
retail_raw = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced_data_quality.csv')

# DATA CLEANSING
# [1] Inspeksi Missing Value untuk masing-masing kolom
print('Check kolom yang memiliki missing data:')
print(retail_raw.isnull().any())
print('\nJumlah missing data pada setiap kolom:')
print(retail_raw.isnull().sum())

# [2] Missing Value Treatments
## [2.1] Filling the missing value using imputation method (imputasi)
print('\nFilling the missing value (imputasi):')
print(retail_raw['quantity'].fillna(retail_raw['quantity'].mean()))

## [2.2] Drop missing value
print('\nDrop missing value:')
print(retail_raw['quantity'].dropna())

# [3] Outliers
## Q1, Q3, dan IQR
Q1 = retail_raw['quantity'].quantile(0.25)
Q3 = retail_raw['quantity'].quantile(0.75)
IQR = Q3 - Q1

## Check ukuran (baris dan kolom) sebelum data yang outliers dibuang
print('\nShape awal: ', retail_raw.shape)

## Removing outliers
retail_raw = retail_raw[~((retail_raw['quantity'] < (Q1 - 1.5 * IQR)) | (retail_raw['quantity'] > (Q3 + 1.5 * IQR)))]

## Check ukuran (baris dan kolom) setelah data yang outliers dibuang
print('Shape akhir: ', retail_raw.shape)

# [4] Data Deduplication
## Check ukuran (baris dan kolom) sebelum data duplikasi dibuang
print('Shape awal: ', retail_raw.shape)

## Buang data yang terduplikasi
retail_raw.drop_duplicates(inplace=True)

## Check ukuran (baris dan kolom) setelah data duplikasi dibuang
print('Shape akhir: ', retail_raw.shape)
