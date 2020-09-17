# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:12:53 2020

@author: jonando93
"""

#Import Library
import pandas as pd

#Membaca File Excel
df = pd.read_excel(r'C:\Users\Asus\Desktop\Jonando\DQLab Case Studies\Python\Supporting Files\df.xlsx')

#Rename Column
df.rename(columns={"Score" : "Nilai"}, inplace=True)

#Menggunakan .groupby
print(df["Nilai"].groupby(df["Name"]).mean())
print(df["Nilai"].groupby([df["Name"], df["Exam"], df["Subject"]]).sum())

#Sorting
print(df.sort_values(by="Name"))


