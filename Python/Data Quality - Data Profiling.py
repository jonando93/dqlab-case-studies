# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:32:29 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import numpy as np
import io
import pandas_profiling

#Membaca Dataset
retail_raw = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced_data_quality.csv')

# DESCRIPTIVE STATISTICS
# [1] Melihat datatype dari setiap kolom di dataset
print(retail_raw.dtypes)

# [2] Melihat len dari kolom di dataset
## Kolom city
length_city = len(retail_raw['city'])
print('Length kolom city:', length_city)

## Tugas Praktek: Kolom product_id
length_product_id = len(retail_raw['product_id'])
print('Length kolom product_id:', length_product_id)

# [3] 
