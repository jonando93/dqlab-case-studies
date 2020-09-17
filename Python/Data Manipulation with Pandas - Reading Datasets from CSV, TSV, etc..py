# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:24:09 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import mysql.connector

#Read Dataset
##File CSV
df_csv = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_csv.csv")
print(df_csv.head(3)) # Menampilkan 3 data teratas

##File TSV
df_tsv = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_tsv.tsv", sep='\t')
print(df_tsv.head(3)) # Menampilkan 3 data teratas

##File Excel
df_excel = pd.read_excel("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/sample_excel.xlsx", sheet_name="test")
print(df_excel.head(4)) # Menampilkan 4 data teratas

##File JSON
url = "https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/covid2019-api-herokuapp-v2.json"
df_json = pd.read_json(url)
print(df_json.head(10)) # Menampilkan 10 data teratas

##File SQL
###1. Membuat koneksi ke database financial di https://relational.fit.cvut.cz/dataset/Financial
my_conn = mysql.connector.connect(host="relational.fit.cvut.cz",
                                  port=3306,
                                  user="guest",
                                  passwd="relational",
                                  database="financial",
                                  use_pure=True)

###2. Membuat query SQL untuk membaca tabel loan
my_query = """
SELECT *
FROM loan;
"""

###3. Menggunakan .read_sql_query untuk membaca tabel loan tersebut
df_loan = pd.read_sql_query(my_query, my_conn) #.read_sql akan menghasilkan output yang sama
print(df_loan.head()) #Menampilkan 5 data teratas

##File Google BigQuery
###1. Membuat query untuk membaca tabel
query = """
SELECT *
FROM 'bigquery-public-data.covid19_jhu_csse_eu.summary'
LIMIT 1000;
"""

###2. Membaca tabel dari Google BigQuery account
df_covid19_eu_summary = pd.read_gbq(query, project_id="XXXXXXXX")
#(Missing optional dependency) print(df_covid_19_eu_summary.head()) #Menampilkan 5 data teratas


