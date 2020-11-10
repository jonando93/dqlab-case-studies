# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:28:58 2020

@author: Asus
"""

#Import Library
import numpy as np
import pandas as pd

#Load Dataset
raw_data = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/dataset_statistic.csv", sep=';')

#Dataset Observation
print('5 Baris Teratas:\n',raw_data.head())
print('\nJumlah Baris pada Dataset:',raw_data.shape[0])
print('\nNama Kolom:\n',raw_data.columns)

#Checking for missing value
print('\nJumlah Missing Value:\n',raw_data.isna().sum())

# [1] UKURAN PUSAT
#Describe Method
print('\nMetode Describe():\n',raw_data.describe())
print('\nMelihat nilai min dari kolom "Harga":',raw_data['Harga'].min())

#Sum Method
print('\nMenghitung jumlah dari semua kolom bertipe data numerik:\n',raw_data.sum(numeric_only=True))

#Mengambil data dari baris ke-0 sampai baris ke-(10-1) atau baris ke-9
## print(raw_data[:10])
 
#Mengambil data dari baris ke-3 sampai baris ke-(5-1) atau baris ke-4
## print(raw_data[3:5])
 
#Mengambil data pada baris ke-1, ke-3 dan ke-10
## print(raw_data.loc[[1,3,10]])

#Mengambil kolom 'Jenis Kelamin' dan 'Pendapatan' dan ambil baris ke-1 sampai ke-9
## print(raw_data[['Jenis Kelamin', 'Pendapatan']][1:10])
 
#Mengambil kolom 'Harga' dan 'Tingkat Kepuasan' dan ambil baris ke-1, ke-10 dan ke-15
## print(raw_data[['Harga', 'Tingkat Kepuasan']].loc[[1,10,15]])

#Mengambil hanya data untuk produk 'A'
produk_A = raw_data[raw_data['Produk'] == 'A']
 
#Menghitung Mean pendapatan menggunakan method .mean pada objek pandas DataFrame
print('\nMean pendapatan untuk produk "A":\n',produk_A['Pendapatan'].mean())
 
#Menghitung Mean pendapatan menggunakan method .mean pada objek pandas DataFrame dengan numpy
#print (np.mean(produk_A['Pendapatan']))

#Menghitung Modus dari kolom 'Produk'
print('\nModus dari masing-masing produk:\n',raw_data['Produk'].value_counts())

#Menghitung Median atau 50% dari kolom 'Pendapatan'
print('\nMedian dari kolom "Pendapatan":\n',raw_data['Pendapatan'].quantile(q = 0.5))

#Menggabungkan (Agregasi) Data dengan metode .agg()
print('')
print(raw_data[['Pendapatan','Harga']].agg([np.mean, np.median]))
print('\n',raw_data[['Pendapatan','Harga','Produk']].groupby('Produk').agg([np.mean, np.median]))

# [2] UKURAN SEBARAN
#Mencari proporsi tiap Produk
print('')
print(raw_data['Produk'].value_counts()/raw_data.shape[0])

#Mencari nilai rentang dari kolom 'Pendapatan'
print (raw_data['Pendapatan'].max() - raw_data['Pendapatan'].min())

#Menghitung variansi umur menggunakan method .var() dari pandas
print (raw_data['Pendapatan'].var()) #Secara default, .var di pandas menggunakan varians sample.
 
#Menghitung variansi umur menggunakan method .var() dari numpy
print (np.var(raw_data['Pendapatan']))

#Mengatur variansi populasi dengan method `.var()` dari pandas
print (raw_data['Pendapatan'].var(ddof=0)) #Dengan menambahkan parameter ddof, maka .var menggunakan varians populasi.

#Menghitung deviasi baku sampel pendapatan menggunakan method std() dari pandas
print (raw_data['Pendapatan'].std())
 
#Menghitung deviasi baku sampel pendapatan menggunakan method std() dari numpy
print (np.std(raw_data['Pendapatan'], ddof = 1))

# [3] KORELASI
#Menghitung korelasi dari setiap pasang variabel pada raw_data
print (raw_data.corr())

#Mencari korelasi 'kendall' untuk tiap pasang variabel
print (raw_data.corr(method='kendall'))
 
#Mencari korelasi 'spearman' untuk tiap pasang variabel
print (raw_data.corr(method='spearman'))
