# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:18:19 2020

@author: jonand93
"""

#Import Library
import pandas as pd

# Dataframe
data = pd.DataFrame({
    'kelas': 6*['A'] + 6*['B'],
    'murid': 2*['A1'] + 2*['A2'] + 2*['A3'] + 2*['B1'] + 2*['B2'] + 2*['B3'],
    'pelajaran': 6*['math','english'],
    'nilai': [90,60,70,85,50,60,100,40,95,80,60,45]
    }, columns=['kelas','murid','pelajaran','nilai'])
print('Dataframe:\n', data)

# Set index data untuk kolom kelas, murid, dan pelajaran
data = data.set_index(['kelas','murid','pelajaran'])
print('Dataframe multi index:\n', data)

# [1] Unstacking dataframe
data_unstack_1 = data.unstack()
print('Unstacking dataframe:\n', data_unstack_1)

# [2] Unstacking dengan specify level name
data_unstack_2 = data.unstack(level='murid')
print('Unstacking dataframe dengan level name:\n', data_unstack_2)

# [3] Unstacking dengan specify level position
data_unstack_3 = data.unstack(level=1)
print('Unstacking dataframe dengan level position:\n', data_unstack_3)

# [1] Stacking dataframe
data_stack = data_unstack_3.stack()
print('Stacked dataframe:\n', data_stack)
# [2] Tukar posisi index setelah stacking dataframe
data_swap = data_stack.swaplevel(1,2)
print('Swapped data:\n', data_swap)
# [3] Melakukan sort_index pada stacking dataframe
data_sort = data_swap.sort_index()
print('Sorted data:\n', data_sort)