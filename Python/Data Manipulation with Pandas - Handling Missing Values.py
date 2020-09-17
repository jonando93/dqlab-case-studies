# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:02:26 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import numpy as np

# Baca file "public data covid19 jhu csse eu.csv"
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/CHAPTER+4+-+missing+value+-+public+data+covid19+.csv")

# Cetak info dari df
print(df.info())

# Cetak jumlah missing value di setiap kolom
mv = df.isna().sum()
print("\nJumlah missing value per kolom:\n", mv)

# Cetak ukuran awal dataframe
print("Ukuran awal df: %d baris, %d kolom." % df.shape) #%d acts as a placeholder for a number. while %s for strings

#METODE 1.1 (Column)- Drop kolom yang seluruhnya missing value dan cetak ukurannya
df = df.dropna(axis=1, how="all") #axis = 1 = "column"
print("Ukuran df setelah buang kolom dengan seluruh data missing: %d baris, %d kolom." % df.shape)

#METODE 1.2 (Row)- Drop baris jika ada satu saja data yang missing dan cetak ukurannya
df = df.dropna(axis=0, how="any") #axis = 0 = "index" atau row
print("Ukuran df setelah dibuang baris yang memiliki sekurangnya 1 missing value: %d baris, %d kolom." % df.shape)

# Cetak unique value pada kolom province_state
print("Unique value awal:\n", df["province_state"].unique())

#METODE 2 (String Data Type)- Ganti missing value dengan string "unknown_province_state"
df["province_state"] = df["province_state"].fillna("unknown_province_state")

# Cetak kembali unique value pada kolom province_state
print("Unique value setelah fillna:\n", df["province_state"].unique())

# Cetak nilai mean dan median awal 
print("Awal: mean = %f, median = %f." % (df["active"].mean(), df["active"].median()))

#METODE 3.1 - Isi missing value kolom active dengan median
df_median = df["active"].fillna(df["active"].median())

# Cetak nilai mean dan median awal setelah diisi dengan median
print("Fillna median: mean = %f, median = %f." % (df_median.mean(), df_median.median()))

#METODE 3.2 - Isi missing value kolom active dengan mean
df_mean = df["active"].fillna(df["active"].mean())

# Cetak nilai mean dan median awal setelah diisi dengan mean
print("Fillna mean: mean = %f, median = %f." % (df_mean.mean(), df_mean.median()))

#METODE 4 - Isi missing value dengan teknik interpolasi
# Data
ts = pd.Series({
   "2020-01-01":9,
   "2020-01-02":np.nan,
   "2020-01-05":np.nan,
   "2020-01-07":24,
   "2020-01-10":np.nan,
   "2020-01-12":np.nan,
   "2020-01-15":33,
   "2020-01-17":np.nan,
   "2020-01-16":40,
   "2020-01-20":45,
   "2020-01-22":52,
   "2020-01-25":75,
   "2020-01-28":np.nan,
   "2020-01-30":np.nan
})
# Isi missing value menggunakan interpolasi linier
ts = ts.interpolate()
# Cetak time series setelah interpolasi linier
print("Setelah diisi missing valuenya:\n", ts)

