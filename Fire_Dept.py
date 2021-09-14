# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:14:59 2021

@author: Srushti
"""

import pandas as pd

df_fdny_data_raw = pd.read_csv('FDNY.csv')

print(df_fdny_data_raw.describe)

print(df_fdny_data_raw.head())


df_fdny_data = pd.read_csv('FDNY.csv',skiprows=(1))
print(df_fdny_data.head(5))

print(df_fdny_data.describe)


print(df_fdny_data.columns)

print(df_fdny_data.index)

print(df_fdny_data.count())

print(df_fdny_data.dtypes)

groupby_borough = df_fdny_data.groupby('Borough')

print(groupby_borough.size())

fdny_info_Manhatten = groupby_borough.get_group('Manhattan')

print(fdny_info_Manhatten)