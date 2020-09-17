# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:20:06 2020

@author: jonando93
"""

#Import Library
import pandas as pd

#Method .append() dapat digunakan pada dataframe/series yang ditujukan untuk menambah row-nya saja.

#Buat series of int (s1) dan series of string (s2)
s1 = pd.Series([1,2,3,4,5,6])
s2 = pd.Series(["a","b","c","d","e","f"])

#Terapkan method append
s1_append_s2 = s1.append(s2)
print("Series - append: \n", s1_append_s2)

#Buat dataframe df1 dan df2
df1 = pd.DataFrame({'a':[1,2],
                    'b':[3,4]})
df2 = pd.DataFrame({'b':[1,2],
                    'a':[3,4]})

#Terapkan method append
df1_append_df2 = df1.append(df2)
print("Dataframe - append: \n", df1_append_df2)

#Method .concat dapat digunakan pada dataframe yang ditujukan untuk 
#penggabungan baik dalam row-wise atau column-wise.

# Terapkan method concat row-wise
row_wise_concat = pd.concat([df2, df1], sort=True)
print("Row-wise - concat:\n", row_wise_concat)
# Terapkan method concat column-wise
col_wise_concat = pd.concat([df2, df1], axis=1, sort=True, keys=["df1", "df2"])
print("Column-wise - concat:\n", col_wise_concat)
# Penambahan identifier --> membentuk hasil penggabungan multiindex
multiindex_concat = pd.concat([df2, df1], axis=0, sort=True, keys=["df1","df2"])
print("Multiindex - concat:\n", multiindex_concat)

#Method .merge() digunakan untuk menggabungkan Series/DataFrame yang bentuknya
#mirip dengan syntax join di SQL

# Buat dataframe df1_merge dan df2_merge
df1_merge = pd.DataFrame({'key':['k1','k2','k3','k4','k5'],
                          'val1':[200, 500, 0, 500, 100],
                          'val2':[30, 50, 100, 20, 10]})
df2_merge = pd.DataFrame({'key':['k1','k3','k5','k7','k10'],
                          'val3':[1,2,3,4,5],
                          'val4':[6,7,8,8,10]})

# Merge yang ekuivalen dengan SQL left join
merge_df_left = pd.merge(left=df2_merge, right=df1_merge, how='left', left_on='key', right_on='key')
print('Merge - Left:\n', merge_df_left)
# Merge yang ekuivalen dengan SQL right join
merge_df_right = pd.merge(left=df2_merge, right=df1_merge, how='right', left_on='key', right_on='key')
print('Merge - Right:\n', merge_df_right)
# Merge yang ekuivalen dengan SQL inner join
merge_df_inner = pd.merge(left=df2_merge, right=df1_merge, how='inner', left_on='key', right_on='key')
print('Merge - Inner:\n', merge_df_inner)
# Merge yang ekuivalen dengan SQL outer join
merge_df_outer = pd.merge(left=df2_merge, right=df1_merge, how='outer', left_on='key', right_on='key')
print('Merge - Outer:\n', merge_df_outer)

#Method .merge() dapat juga digunakan untuk dataframe yang memiliki multiindex

# Buat dataframe df1_multi dan df2_multi
df1_multi = pd.DataFrame({'key':['k1','k2','k3','k4','k5'],
                          'val1':[200, 500, 0, 500, 100],
                          'val2':[30, 50, 100, 20, 10]}).set_index(['key','val2'])
print('DataFrame 1:\n', df1_multi)
df2_multi = pd.DataFrame({'key':['k1','k3','k5','k7','k10'],
                          'val3':[1,2,3,4,5],
                          'val4':[6,7,8,8,10]}).set_index(['key','val3'])
print('DataFrame 2:\n', df2_multi)

# Merge dataframe yang memiliki multi index
df_multi_merge = pd.merge(df1_multi.reset_index(),df2_multi.reset_index())
print('Merging dataframe:\n', df_multi_merge)

#Method .join() digunakan pada dataframe untuk menggabungkan kedua data dengan
#set index pada kedua tabel tersebut sebagai join key, tanpa index, hal ini 
#tidak akan 

# Buat dataframe df1_join dan df2_join
df1_join = pd.DataFrame({'key':['k1','k2','k3','k4','k5'],
                         'val1':[200, 500, 0, 500, 100],
                         'val2':[30, 50, 100, 20, 10]})
df2_join = pd.DataFrame({'key':['k1','k3','k5','k7','k10'],
                    'val3':[1,2,3,4,5],
                    'val4':[6,7,8,8,10]})

# Penerapan join dengan menggunakan set_index dan keyword how
join_df = df1_join.set_index('key').join(df2_join.set_index('key'), how='outer')
print(join_df)





