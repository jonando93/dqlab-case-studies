# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:19:41 2020

@author: Asus
"""

#DQLab Data Science Challenge with Python

##Menggabungkan Dictionary Data.
dict1 = {1:10, 2:20}
dict2 = dict1.update({3:30, 4:40})
dict3 = dict1.update({5:50, 6:60})
dict4 = {}

for key in dict1:
    dict4[key] = dict1[key]

print(dict4)


##Menghitung Jumlah 7 Deret Pertama Fibonacci
# - Buat Fungsi Fibonacci
def calculateSum(n):
    if n <= 0:
        return 0
    fibo = [0] * (n+1)
    fibo[1] = 1
    # - Initialisasi hasil ke dalam variabel sm
    sm = fibo[0] + fibo[1]
    # - Tambahkan suku-suku berikutnya
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2] 
        sm += fibo[i]
    return sm
# - Evaluasi hasil deret untuk n = 7    
print(calculateSum(7))
