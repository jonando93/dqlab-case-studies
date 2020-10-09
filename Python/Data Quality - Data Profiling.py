# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:32:29 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import numpy as np
import io
import pandas_profiling as pp

#Membaca Dataset
retail_raw = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced_data_quality.csv')

# DESCRIPTIVE STATISTICS
# [1] Inspeksi datatype dari setiap kolom di dataset
print(retail_raw.dtypes)

# [2] Melihat len dari kolom di dataset
## Kolom city
length_city = len(retail_raw['city'])
print('\nLength kolom city:', length_city)

## Tugas Praktek: Kolom product_id
length_product_id = len(retail_raw['product_id'])
print('Length kolom product_id:', length_product_id)

# [3] Menghitung jumlah non-NA dalam suatu kolom
# Count kolom city
count_city = retail_raw['city'].count()
print('\nCount kolom city:', count_city)

# Tugas praktek: count kolom product_id
count_product_id = retail_raw['product_id'].count()
print('Count kolom product_id:', count_product_id)

# [4] Inspeksi missing value pada masing-masing kolom
## Missing value pada kolom city
number_of_missing_values_city = length_city - count_city
float_of_missing_values_city = float(number_of_missing_values_city/length_city)
pct_of_missing_values_city = '{0:.1f}%'.format(float_of_missing_values_city * 100) #{0:f} adalah f conversion type argument untuk persentase. .1f = 1 angka di blkg koma
print('\nPersentase missing value kolom city:', pct_of_missing_values_city)

## Tugas praktek: Missing value pada kolom product_id
number_of_missing_values_product_id = length_product_id - count_product_id
float_of_missing_values_product_id = float(number_of_missing_values_product_id/length_product_id)
pct_of_missing_values_product_id = '{0:.1f}%'.format(float_of_missing_values_product_id * 100)
print('Persentase missing value kolom product_id:', pct_of_missing_values_product_id)

# [5] Descriptive Statistics
## Deskriptif statistics kolom quantity
print('Kolom quantity')
print('Minimum value: ', retail_raw['quantity'].min())
print('Maximum value: ', retail_raw['quantity'].max())
print('Mean value: ', retail_raw['quantity'].mean())
print('Mode value: ', retail_raw['quantity'].mode())
print('Median value: ', retail_raw['quantity'].median())
print('Standard Deviation value: ', retail_raw['quantity'].std())

## Tugas praktek: Deskriptif statistics kolom item_price
print('')
print('Kolom item_price')
print('Minimum value: ', retail_raw['item_price'].min())
print('Maximum value: ', retail_raw['item_price'].max())
print('Mean value: ', retail_raw['item_price'].mean())
print('Median value: ', retail_raw['item_price'].median())
print('Standard Deviation value: ', retail_raw['item_price'].std())

# [6] Quantile Statistics
## Quantile statistics kolom quantity
print('\nKolom quantity:')
print(retail_raw['quantity'].quantile([0.25, 0.5, 0.75]))

## Tugas praktek: Quantile statistics kolom item_price
print('')
print('Kolom item_price:')
print(retail_raw['item_price'].quantile([0.25, 0.5, 0.75]))

# [7] Correlation
print('Korelasi quantity dengan item_price')
print(retail_raw[['quantity', 'item_price']].corr())

# [8] Profiling Library - Pandas Profiling
report = pp.ProfileReport(retail_raw)
report.to_file('profile_report.html')