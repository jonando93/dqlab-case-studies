# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:14:53 2020

@author: jonando93
"""

#Import Library
import pandas as pd

#Membaca File Excel
order_df = pd.read_excel(r'C:\Users\Asus\Desktop\Jonando\DQLab Case Studies\Python\Supporting Files\coalpublic2013-1.xls')

#Standar Deviasi & Varians
print("Varians = " + str(order_df.loc[:, "Average Employees"].std()))
print("Standar Deviasi = " + str(order_df.loc[:, "Average Employees"].var()))

#Interquartile
Q1 = order_df[["Average Employees"]].quantile(0.25)
Q3 = order_df[["Average Employees"]].quantile(0.75)
IQR = Q3 - Q1
print(IQR)