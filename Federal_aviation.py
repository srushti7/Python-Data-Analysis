# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:24:26 2021

@author: Srushti
"""

import pandas as pd
import csv as csv

daa_faa_dataset = pd.read_csv('faa_ai_prelim.csv')
print(daa_faa_dataset.shape) #view dataset shape


print(daa_faa_dataset.head()) #view first 5 records

print(daa_faa_dataset.columns) #view columns



df_analyse_dataset = daa_faa_dataset[['ACFT_MAKE_NAME', 'LOC_STATE_NAME','ACFT_MODEL_NAME','RMK_TEXT','FLT_PHASE','EVENT_TYPE_DESC','FATAL_FLAG']]

#view first 5 observations

print(df_analyse_dataset)

print(type(df_analyse_dataset)) #view type
print(df_analyse_dataset.head())#first 5 records of the dataframe

print(df_analyse_dataset['FATAL_FLAG'].fillna(value='No', inplace=True)) #fill NaN values with No

print(df_analyse_dataset.head()) # view first five records


print(df_analyse_dataset.shape)

df_final_dataset = df_analyse_dataset.dropna(subset=['ACFT_MAKE_NAME'])  #drop values

print(df_final_dataset.shape)

aircraftType = df_final_dataset.groupby('ACFT_MAKE_NAME')

print(aircraftType.size())

fatalAccidents = df_final_dataset.groupby('FATAL_FLAG')

print(fatalAccidents.size())

accidents_with_fatality = fatalAccidents.get_group('Yes')
print(accidents_with_fatality)
