# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:27:39 2020

@author: jonando93
"""

#Import Library
import pandas as pd
import numpy as np

#List
##Creating Series from List
ex_list = ['a', 1, 3, 5, 'c', 'd']
ex_series = pd.Series(ex_list)
print(ex_series)

##Creating DataFrame from List of List
ex_list_of_list = [[1, 'a', 'b', 'c'],
                   [2.5, 'd', 'e', 'f'],
                   [5, 'g', 'h', 'i'],
                   [7.5, 'j', 10.5, 'l']]
index = ['dq', 'lab', 'kar', 'lan']
cols = ['float', 'char', 'obj', 'char']
ex_df = pd.DataFrame(ex_list_of_list, index=index, columns=cols)
print(ex_df)

#Dictionary
##Creating Series from Dictionary
dict_series = {'1':'a',
			   '2':'b',
			   '3':'c'}
ex_dictseries = pd.Series(dict_series)
print(ex_dictseries)

##Creating DataFrame from Dictionary
df_series = {'1':['a','b','c'],
             '2':['b','c','d'],
             '4':[2,3,'z']}
ex_dictdf = pd.DataFrame(df_series)
print(ex_dictdf)

#Numpy Array
##Creating series from numpy array (1D)
arr_series = np.array([1,2,3,4,5,6,6,7])
ex_arrseries = pd.Series(arr_series)
print(ex_arrseries)

##Creating dataframe from numpy array (2D)
arr_df = np.array([[1, 2, 3, 5],
                   [5, 6, 7, 8],
                   ['a','b','c',10]])
ex_arrdf = pd.DataFrame(arr_df)
print(ex_arrdf)

