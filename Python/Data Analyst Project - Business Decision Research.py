# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:28:37 2020

@author: jonando93
"""

# DATA ANALYST PROJECT: BUSINESS DECISION RESEARCH


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#Background:
#DQLab sport center adalah toko yang menjual berbagai kebutuhan olahraga 
#seperti Jaket, Baju, Tas, dan Sepatu. Toko ini mulai berjualan sejak tahun 
#2013, sehingga sudah memiliki pelanggan tetap sejak lama, dan tetap berusaha 
#untuk mendapatkan pelanggan baru sampai saat ini.
#
#Di awal tahun 2019,   manajer toko tersebut merekrut junior DA untuk membantu
#memecahkan masalah yang ada di tokonya, yaitu menurunnya pelanggan yang 
#membeli kembali ke tokonya.  Junior DA tersebut pun diberi kepercayaan 
#mengolah data transaksi toko tersebut. Manajer toko mendefinisikan bahwa 
#customer termasuk sudah bukan disebut pelanggan lagi (churn) ketika dia sudah
#tidak bertransaksi ke tokonya lagi sampai dengan 6 bulan terakhir dari update 
#data terakhir yang tersedia.  
#
#Manajer toko pun memberikan data transaksi dari tahun 2013 sampai dengan 2019 
#dalam bentuk csv (comma separated value) dengan data_retail.csv dengan jumlah 
#baris 100.000 baris data.
#
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# MARKET RESEARCH ,RECOMMENDATION AND VISUALIZATION TECHNIQUE FOR BUSINESS 
# DECISION MAKING

# Import Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca Dataframe
df = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/data_retail.csv', sep=';')

print('Lima data teratas:')
print(df.head())

print('\nInfo dataset:')
print(df.info())

# [1] DATA CLEANSING
## [1.1] Converting Datatype
### Kolom First_Transaction
df['First_Transaction'] = pd.to_datetime(df['First_Transaction']/1000, unit='s', origin='1970-01-01')
### Kolom Last_Transaction
df['Last_Transaction'] = pd.to_datetime(df['Last_Transaction']/1000, unit='s', origin='1970-01-01')

print('Lima data teratas:')
print(df.head())

print('\nInfo dataset:')
print(df.info())

## [1.2] Pengecekan transaksaksi terakhir dalam dataset
print(max(df['Last_Transaction']))

## [1.3] Klasifikasikan customer yang berstatus churn atau tidak dengan boolean
df.loc[df['Last_Transaction']<='2018-08-01', 'is_churn'] = True #Kita dapat membuat kolom baru dengan fungsi loc
df.loc[df['Last_Transaction']>'2018-08-01', 'is_churn'] = False #Kolom baru yang kita buat yaitu 'is_churn'

print('Lima data teratas:')
print(df.head())

print('\nInfo dataset:')
print(df.info())

## [1.4] Hapus kolom-kolom yang tidak diperlukan
df = df.drop(['no', 'Row_Num'], axis=1)

print('Lima data teratas:')
print(df.head())

print('\nInfo dataset:')
print(df.info())

# [2] DATA VISUALIZATION
## [2.1] Trend of Customer Acquisition by Year
### Kolom tahun transaksi pertama
df['Year_First_Transaction'] = df['First_Transaction'].dt.year
### Kolom tahun transaksi terakhir
df['Year_Last_Transaction'] = df['Last_Transaction'].dt.year

df_year = df.groupby(['Year_First_Transaction'])['Customer_ID'].count()
df_year.plot(x='Year_First_Transaction', y='Customer_ID', kind='bar', title='Graph of Customer Acquisition')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

## [2.2] Trend of Customer Transaction by Year
plt.clf()
df_year = df.groupby(['Year_First_Transaction'])['Count_Transaction'].sum()
df_year.plot(x='Year_First_Transaction', y='Count_Transaction', kind='bar', title='Graph of Transaction Customer')
plt.xlabel('Year_First_Transaction')
plt.ylabel('Num_of_Transaction')
plt.tight_layout()
plt.show()

## [2.3] Average Transaction Amount by Year
plt.clf()
sns.pointplot(data = df.groupby(['Product', 'Year_First_Transaction']).mean().reset_index(), 
              x='Year_First_Transaction', 
              y='Average_Transaction_Amount', 
              hue='Product')
plt.tight_layout()
plt.show()

## [2.4] Churned Customer Proportion by Product
plt.clf()
### Melakukan pivot data dengan pivot_table
df_piv = df.pivot_table(index='is_churn', 
                        columns='Product',
                        values='Customer_ID', 
                        aggfunc='count', 
                        fill_value=0)

### Mendapatkan Proportion Churn by Product
plot_product = df_piv.count().sort_values(ascending=False).head(5).index

### Plot pie chartnya
df_piv = df_piv.reindex(columns=plot_product)
df_piv.plot.pie(subplots=True,
                figsize=(10, 7),
                layout=(-1, 2),
                autopct='%1.0f%%',
                title='Proportion Churn by Product')
plt.tight_layout()
plt.show()