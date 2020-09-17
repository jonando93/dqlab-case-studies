# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:33:41 2020

@author: jonando93
"""

#Import Library
import pandas as pd

# Load data global_air_quality.csv
global_air_quality = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv')
print('Lima data teratas:\n', global_air_quality.head())

# Melakukan pengecekan terhadap data
print('Info global_air_quality:\n', global_air_quality.info())

# Melakukan count tanpa groupby
print('Count tanpa groupby:\n', global_air_quality.count())

# Melakukan count dengan groupby 
gaq_groupby_count = global_air_quality.groupby('source_name').count()
print('Count dengan groupby (5 data teratas):\n', gaq_groupby_count.head())

# Create variabel pollutant 
pollutant = global_air_quality[['country','city','pollutant','value']].pivot_table(index=['country','city'],columns='pollutant').fillna(0)
print('Data pollutant (5 teratas):\n', pollutant.head())

# [1] Group berdasarkan country dan terapkan aggregasi mean
pollutant_mean = pollutant.groupby('country').mean()
print('Rata-rata pollutant (5 teratas):\n', pollutant_mean.head())

# [2] Group berdasarkan country dan terapkan aggregasi std
pollutant_std = pollutant.groupby('country').std().fillna(0)
print('Standar deviasi pollutant (5 teratas):\n', pollutant_std.head())

# [3] Group berdasarkan country dan terapkan aggregasi sum
pollutant_sum = pollutant.groupby('country').sum()
print('Total pollutant (5 teratas):\n', pollutant_sum.head())

# [4] Group berdasarkan country dan terapkan aggregasi nunique
pollutant_nunique = pollutant.groupby('country').nunique()
print('Jumlah unique value pollutant (5 teratas):\n', pollutant_nunique.head())

# [5] Group berdasarkan country dan terapkan aggregasi first
pollutant_min = pollutant.groupby('country').min()
print('Nilai min pollutant (5 teratas):\n', pollutant_min.head())

# [6] Group berdasarkan country dan terapkan aggregasi last
pollutant_max = pollutant.groupby('country').max()
print('Nilai max pollutant (5 teratas):\n', pollutant_max.head())

# [7] Group berdasarkan country dan terapkan aggregasi first
pollutant_first = pollutant.groupby('country').first()
print('Item pertama pollutant (5 teratas):\n', pollutant_first.head())

# [8] Group berdasarkan country dan terapkan aggregasi last
pollutant_last = pollutant.groupby('country').last()
print('Item terakhir pollutant (5 teratas):\n', pollutant_last.head())

# [9] Group berdasarkan country dan terapkan (Multiple Aggregation) aggregasi: min, median, mean, max
multiagg = pollutant.groupby('country').agg(['min','median','mean','max'])
print('Multiple aggregations (5 teratas):\n', multiagg.head())

# Create sebuah function: iqr
def iqr(series):
	Q1 = series.quantile(0.25)
	Q3 = series.quantile(0.75)
	return Q3 - Q1

# [10] Group berdasarkan country dan terapkan (Custom Aggregations) aggregasi dari function: iqr
custom_agg = pollutant.groupby('country')
print('Custom aggregation (5 teratas):\n', custom_agg.apply(iqr).head())

# [11] Create custom aggregation using dict
custom_agg_dict = pollutant['value'][['pm10','pm25','so2']].groupby('country').agg({
   'pm10':'median',
   'pm25':iqr,
   'so2':iqr
})
print('\nCetak 5 data teratas custom_agg_dict:\n', custom_agg_dict.head())