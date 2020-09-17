# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:50:41 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import matplotlib.pyplot as plt

#Membaca File Excel
order_df = pd.read_excel(r'C:\Users\Asus\Desktop\Jonando\DQLab Case Studies\Python\Supporting Files\coalpublic2013-1.xls')

#Plot Histogram
order_df[["Average Employees"]].plot.hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()
