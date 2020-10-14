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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Membaca Dataframe
df = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/data_retail.csv', sep=';')

print('Lima data teratas:')
print(df.head())

print('\nInfo dataset:')
print(df.info())

# [1] DATA CLEANSING
## [1.1] Converting Datatype
### [1.1.1] Kolom First_Transaction
df['First_Transaction'] = pd.to_datetime(df['First_Transaction']/1000, unit='s', origin='1970-01-01')
### [1.1.2] Kolom Last_Transaction
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
### [2.1.1] Kolom tahun transaksi pertama
df['Year_First_Transaction'] = df['First_Transaction'].dt.year
### [2.1.2] Kolom tahun transaksi terakhir
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
### [2.4.1] Melakukan pivot data dengan pivot_table
df_piv = df.pivot_table(index='is_churn', 
                        columns='Product',
                        values='Customer_ID', 
                        aggfunc='count', 
                        fill_value=0)

### [2.4.2] Mendapatkan Proportion Churn by Product
plot_product = df_piv.count().sort_values(ascending=False).head(5).index

### [2.4.3] Plot pie chartnya
df_piv = df_piv.reindex(columns=plot_product)
df_piv.plot.pie(subplots=True,
                figsize=(10, 7),
                layout=(-1, 2),
                autopct='%1.0f%%',
                title='Proportion Churn by Product')
plt.tight_layout()
plt.show()

## [2.5] Distribution of Count Transaction Categorization
plt.clf()
### [2.5.1] Kategorisasi jumlah transaksi
def func(row):
    if row['Count_Transaction'] == 1:
        val = '1. 1'
    elif (row['Count_Transaction'] > 1 and row['Count_Transaction'] <= 3):
        val ='2.2 - 3'
    elif (row['Count_Transaction'] > 3 and row['Count_Transaction'] <= 6):
        val ='3.4 - 6'
    elif (row['Count_Transaction'] > 6 and row['Count_Transaction'] <= 10):
        val ='4.7 - 10'
    else:
        val ='5.> 10'
    return val

### [2.5.2] Tambahkan kolom baru
df['Count_Transaction_Group'] = df.apply(func, axis=1)

df_year = df.groupby(['Count_Transaction_Group'])['Customer_ID'].count()
df_year.plot(x='Count_Transaction_Group', y='Customer_ID', kind='bar', title='Customer Distribution by Count Transaction Group')
plt.xlabel('Count_Transaction_Group')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

## [2.6] Distribution of Average Transaction Amount Categorization
plt.clf()
### [2.6.1] Kategorisasi rata-rata besar transaksi
def f(row):
    if (row['Average_Transaction_Amount'] >= 0 and row['Average_Transaction_Amount'] <= 100000):
        val ='1. 0 - 100.000'
    elif (row['Average_Transaction_Amount'] > 100000 and row['Average_Transaction_Amount'] <= 250000):
        val ='2. >100.000 - 250.000'
    elif (row['Average_Transaction_Amount'] > 250000 and row['Average_Transaction_Amount'] <= 500000):
        val ='3. >250.000 - 500.000'
    elif (row['Average_Transaction_Amount'] > 500000 and row['Average_Transaction_Amount'] <= 750000):
        val ='4. >500.000 - 750.000'
    elif (row['Average_Transaction_Amount'] > 750000 and row['Average_Transaction_Amount'] <= 1000000):
        val ='5. >750.000 - 1.000.000'
    elif (row['Average_Transaction_Amount'] > 1000000 and row['Average_Transaction_Amount'] <= 2500000):
        val ='6. >1.000.000 - 2.500.000'
    elif (row['Average_Transaction_Amount'] > 2500000 and row['Average_Transaction_Amount'] <= 5000000):
        val ='7. >2.500.000 - 5.000.000'
    elif (row['Average_Transaction_Amount'] > 5000000 and row['Average_Transaction_Amount'] <= 10000000):
        val ='8. >5.000.000 - 10.000.000'
    else:
        val ='9. >10.000.000'
    return val

### [2.6.2] Tambahkan kolom baru
df['Average_Transaction_Amount_Group'] = df.apply(f, axis=1)

df_year = df.groupby(['Average_Transaction_Amount_Group'])['Customer_ID'].count()
df_year.plot(x='Average_Transaction_Amount_Group', y='Customer_ID', kind='bar', title='Customer Distribution by Average Transaction Amount Group')
plt.xlabel('Average_Transaction_Amount_Group')
plt.ylabel('Num_of_Customer')
plt.tight_layout()
plt.show()

# [3] DATA MODELLING
## [3.1] Configuring Feature & Target Columns
### [3.1.1] Feature column: Year_Diff
df['Year_Diff'] = df['Year_Last_Transaction'] - df['Year_First_Transaction']

### [3.1.2] Nama-nama feature columns
feature_columns = ['Average_Transaction_Amount', 'Count_Transaction', 'Year_Diff']

### [3.1.3] Features variable
X = df[feature_columns] 

### [3.1.4] Target variable
y = df['is_churn']
y = df['is_churn'].astype('int64')

## [3.2] Configuring Training Set & Test Set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=0)

## [3.3] Train, Predict, Evaluate Model
### [3.3.1] Inisiasi model logreg
logreg = LogisticRegression()

### [3.3.2] Fit the model with data
logreg = logreg.fit(X_train, y_train)

### [3.3.3] Predict model
y_pred = logreg.predict(X_test)

### [3.3.4] Evaluasi model menggunakan confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', cnf_matrix)

## [3.3] Confusion Matrix Visualization
plt.clf()
### [3.3.1] Name  of Classes
class_names = [0, 1] 
fig, ax = plt.subplots()

tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

### [3.3.2] Create heatmap
sns.heatmap(cnf_matrix, annot=True, cmap='YlGnBu', fmt='g')
ax.xaxis.set_label_position('top')
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.tight_layout()
plt.show()

## [3.4] Accuracy, Precision, and Recall
### [3.4.1] Menghitung Accuracy, Precision, dan Recall
print('Accuracy :', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred, average='micro'))
print('Recall   :', recall_score(y_test, y_pred, average='micro'))