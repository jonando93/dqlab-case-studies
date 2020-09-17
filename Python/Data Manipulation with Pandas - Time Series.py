# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:43:59 2020

@author: jonando93
"""

#Import Library
import pandas as pd

#Load Dataset as Time Series
gaq_parse = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv', parse_dates=True, index_col='timestamp')

# Cetak 5 data teratas dari dataframe gaq_parse
print(gaq_parse.head())

# Cetak info dari dataframe gaq_parse
print('info')
print(gaq_parse.info())

# Load Dataset
gaq = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv')

# Cetak 5 Data teratas
print('Sebelum diubah dalam format datetime:\n', gaq.head())

# Ubah menjadi datetime
gaq['timestamp'] = pd.to_datetime(gaq['timestamp'])
gaq = gaq.set_index('timestamp')

# Cetak 5 data teratas
print('Sesudah diubah dalam format datetime:\n', gaq.head())

