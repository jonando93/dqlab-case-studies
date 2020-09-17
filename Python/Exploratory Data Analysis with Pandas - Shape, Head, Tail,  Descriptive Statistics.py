# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:14:24 2020

@author: jonando93
"""
#Melakukan import library Pandas
import pandas as pd

#Membaca file excel
dummy_data = pd.read_excel(r'C:\Users\Asus\Desktop\Jonando\DQLab Case Studies\Python\Supporting Files\coalpublic2013-1.xls')

#Melihat struktur kolom dan baris dari data frame
print(dummy_data.shape)

#Melihat preview data dari data frame
##Menampilkan konten teratas dari dummy_data
print(dummy_data.head())

##Menampilkan konten terbawah dari dummy_data
print(dummy_data.tail())

#Statistik Deskriptif dari data frame - Part 1
print(dummy_data.describe(include="all")) #jika ingin mendapat summary dari kolom karakter, ubah "all" ke "object"

#Statistik Deskriptif dari data frame - Part 2
print(dummy_data.loc[:, "Production (short tons)"].mean())
print(dummy_data.loc[:, "Production (short tons)"].median())
print(dummy_data.loc[:, "Production (short tons)"].mode())