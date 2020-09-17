# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:40:04 2020

@author: jonando93
"""

import pandas as pd

# Baca file TSV sample_tsv.tsv
df = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv", sep="\t")

#Indexing - Single Index
## Index dari df
print("Index:", df.index)
## Column dari df
print("Columns:", df.columns)

#Indexing - Hierarchical Index (Multi Index)
## Set Multi Index
df_x = df.set_index(['order_id', 'customer_id', 'product_id', 'order_date'])
print(df_x)

##Index dari df_x
print("Index df_x:", df_x.index)

##Print Names and Levels from Multi Index
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name, ":", level)

#Define and Assign Index
##Creating DataFrame
df_week = pd.DataFrame({
    "day_number" : [1,2,3,4,5,6,7],
    "week_type" : ["weekday" for i in range(5)] + ["weekend" for i in range(2)]})

##Defining and Assinging Index
df_week.index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(df_week)

#CASE EXAMPLE
# Baca file sample_tsv.tsv untuk 10 baris pertama saja
df_case = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv", sep="\t", nrows=10)
# Cetak data frame awal
print("Dataframe awal:\n", df_case)
# Set index baru
df_case.index = ["Pesanan ke-" + str(i) for i in range(1, 11)]
# Cetak data frame dengan index baru
print("Dataframe dengan index baru:\n", df_case)

# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df_example = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv", sep="\t", index_col=["order_date", "order_id"])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df_example.head(8))
