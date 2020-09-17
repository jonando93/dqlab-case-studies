# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:03:46 2020

@author: jonando93
"""
#Import Library
import pandas as pd
import matplotlib.pyplot as plt

#Resampling dibagi menjadi 2:
#1. Downsampling - Contoh: Daily to Weekly
#2. Upsampling - Contoh: Yearly to Monthly

#Resampling untuk Time Series:
#'Min' - Minute
#'H' - Hour
#'D' - Day
#'B' - Business Day
#'W' - Week
#'M' - Month
#'Q' - Quarterly
#'A' - Annual/Year

# Load dataset Global Air Quality
gaq = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/LO4/global_air_quality_4000rows.csv')
gaq['timestamp'] = pd.to_datetime(gaq['timestamp'])
gaq = gaq.set_index('timestamp')
print('Dataset sebelum di-downsampling (5 teratas):\n', gaq.head())


# [1] Downsampling dari daily to weekly dan kita hitung maksimum untuk seminggu
gaq_weekly = gaq.resample('W')
print('Downsampling daily to weekly - max (5 teratas):\n', gaq_weekly)

# [2] Downsampling dari daily to quaterly dan kita hitung minimumnya untuk tiap quarter
gaq_quarterly = gaq.resample('Q')
print('Downsampling daily to quaterly - min (5 teratas):\n', gaq_quarterly)

# [3.1] Membuat pivot table yang menunjukkan waktu di baris nya dan masing-masing value dari pollutant nya dalam kolom
gaq_viz = gaq[['pollutant','value']].reset_index().set_index(['timestamp','pollutant'])
gaq_viz = gaq_viz.pivot_table(index='timestamp', columns='pollutant', aggfunc='mean').fillna(0)
gaq_viz.columns = gaq_viz.columns.droplevel(0)
print('Data (5 teratas):\n', gaq_viz.head())

# [3.2] Membuat fungsi yang memberikan default value 0 ketika value nya di bawah 0 dan apply ke setiap elemen dari dataset tersebut, kemudian menampilkannya sebagai chart
def default_val(val):
 if val < 0:
   return 0
 else:
   return val
line1 = gaq_viz.resample('M').mean().ffill().applymap(lambda x: default_val(x)).apply(lambda x: x/x.max()) # default value if value < 0 then 0, kemudian menghasilkan % value = value/max(value)
line1.plot(
   title = 'average value of each pollutant over months',
   figsize = (10,10), #ukuran canvas 10px x 10px
   ylim = (0,1.25), #memberikan batas tampilan y-axis hanya 0 sampai 125%
   subplots = True #memecah plot menjadi beberapa bagian sesuai dengan jumlah kolom
)
plt.ylabel('avg pollutant (%)')
plt.xlabel('month')
plt.show()



