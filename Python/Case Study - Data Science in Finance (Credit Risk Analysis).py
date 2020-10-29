# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 13:35:16 2020

@author: jonando93
"""

#Import Library
import pandas as pd

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