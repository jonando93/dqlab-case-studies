# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:03:58 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import datetime
import matplotlib.pyplot as plt

#Membaca Dataset
dataset = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv')
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

#[1] Data Preparation
## Penambahan Kolom 'Order Month' pada Dataset
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
print(dataset.head())

##Penambahan Kolom 'GMV' pada Dataset
dataset['gmv'] = dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

#[2.1] Default Plot using Matplotlib
##Membuat monthly amount untuk dijadikan graphic (Data Agregat)
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)

##Membuat Line Chart Trend Pertumbuhan GMV
plt.plot(monthly_amount['order_month'], monthly_amount['gmv']) #Default parameter fungsi plt.plot yaitu (x, y)
plt.show()

##Cara Alternatif Membuat Line Chart Trend Pertumbuhan GMV menggunakan fungsi .plot
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

#[2.2] Graph Customization - Search for "Matplotlib Anatomy" in Google to understand more about matplotlib
##Mengubah Figure Size & Parameter fungsi .plot()
fig = plt.figure(figsize=(15,5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)

##Menambahkan Title dan Axis Labels & Parameternya
plt.title('Monthly GMV Year 2019', loc='center', pad=40, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total GMV (in Billions)', fontsize=15)

##Menambahkan Grid & Parameternya
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

##Menentukan Batas Min (juga dapat digunakan untuk Max) & Parameternya (xlim untuk sumbu x)
plt.ylim(ymin=0)

##Mengubah Axis Ticks & Parameternya
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))

##Menambahkan Text pada Plot
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019', transform=fig.transFigure, color='red')

#Menyimpan Hasil Plot Menjadi File
plt.savefig('monthly_gmv.pdf', bbox_inches='tight')
plt.show()

#Code untuk melihat format apa saja yang dapat digunakan untuk menyimpan file
plt.gcf().canvas.get_supported_filetypes()







