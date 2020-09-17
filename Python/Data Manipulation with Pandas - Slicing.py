# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:39:40 2020

@author: jonando93
"""

#Import Library
import pandas as pd

#Baca file sample_csv.csv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")

#Slice berdasarkan kolom
df_slice_col = df.loc[(df["customer_id"] == 18055) & (df["product_id"].isin(["P0029", "P0040", "P0041", "P0116", "P0117"]))]
print("Slice langsung berdasarkan kolom:\n", df_slice_col)

#Slice berdasarkan index - 2 Steps
##Step 1
##Set index dari DataFrame menggunakan set_index
df1 = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
df1 = df1.set_index(["order_date", "order_id", "product_id"])
##Slice berdasar index
df_slice1 = df1.loc[("2019-01-01", 1612339, ["P2154","P2159"]),:]
print("Slice df - Step 1:\n", df_slice1)

##Step 2
df2 = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
df2 = df2.set_index(["order_date","product_id"])
idx = pd.IndexSlice
df_slice2 = df2.sort_index().loc[idx["2019-01-01", "P2154":"P2556"], :]
print("Slice df - Step 2:\n", df_slice2)

