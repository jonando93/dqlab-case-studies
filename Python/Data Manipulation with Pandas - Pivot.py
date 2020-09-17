# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 16:34:55 2020

@author: jonando93
"""

# Import Library
import pandas as pd

# DataFrame
data = pd.DataFrame({
    'kelas' : 6*['A'] + 6*['B'],
    'murid' : 2*['A1'] + 2*['A2'] + 2*['A3'] + 2*['B1'] + 2*['B2'] + 2*['B3'],
    'pelajaran' : 6*['math','english'],
    'nilai' : [90, 60, 70, 85, 50, 60, 100, 40, 95, 80, 60, 45]
    }, columns = ['kelas','murid','pelajaran','nilai'])

# Unique value pada setiap kolom data
for column in data.columns:
    print('Unique value %s: %s' % (column, data[column].unique()))
    
# Pivoting with single column measurement
pivot1 = data.pivot(index='murid', columns='pelajaran', values='nilai')
print('Pivoting with single column measurement:\n', pivot1)

# Pivoting with multiple column measurement
pivot2 = data.pivot(index='murid', columns='pelajaran')
print('Pivoting with multiple column measurement:\n', pivot2)

# Pivoting with duplicate index
##Creating pivot and assign pivot_tab dengan menggunakan keyword aggfunc=sum
pivot_tab_sum = data.pivot_table(index='kelas',columns='pelajaran',values='nilai',aggfunc=sum)
print('Creating pivot table -- aggfunc mean:\n', pivot_tab_sum)

##Creating pivot and assign pivot_tab dengan menggunakan keyword aggfunc='mean'
pivot_tab_mean = data.pivot_table(index='kelas',columns='pelajaran',values='nilai',aggfunc='mean')
print('Creating pivot table -- aggfunc mean:\n', pivot_tab_mean)

##Creating pivot and assign pivot_tab dengan menggunakan keyword aggfunc='median'
pivot_tab_median = data.pivot_table(index='kelas',columns='pelajaran',values='nilai',aggfunc='median')
print('Creating pivot table -- aggfunc median:\n', pivot_tab_median)