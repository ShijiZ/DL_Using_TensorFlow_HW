#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:20:16 2019

@author: shijizhao
"""

## Problem 1
print('Problem 1')
import pandas as pd

py_list = ['Golden State', '49ers', 'Giants', 
           'Cavaliers', 'Lakers', 'Rams', 'Yankees']

team_series1 = pd.Series(py_list)

print(team_series1)
print()

## Problem 2
print('Problem 2')
import pandas as pd

py_dict = {'Oakland-Basketball':'Golden State',
           'SF-Football':'49ers', 
           'SF-Baseball':'Giants',
           'Cleveland-Basketball':'Cavaliers', 
           'LA-Basketball':'Lakers',
           'LA-Football':'Rams', 
           'NY-Baseball':'Yankees'}

team_series2 = pd.Series(py_dict)

print(team_series2)
print()

## Problem 3
print('Problem 3')
# The 5th and 7th element of team_series1
print(team_series1.loc[4])
print(team_series1.loc[6])
print(team_series1.iloc[4])
print(team_series1.iloc[6])

# The 5th and 7th element of team_series2
print(team_series2.loc['LA-Basketball'])
print(team_series2.loc['NY-Baseball'])
print(team_series2.iloc[4])
print(team_series2.iloc[6])
print()

## Problem 4
print('Problem 4')
import pandas as pd
import numpy as np

num = pd.Series(range(1,101))

# for loop summation
sum1 = 0
for i in num:
    sum1 += i
    
print(sum1)

# numpy summation
sum2 = np.sum(num)
print(sum2)
print()

## Problem 5
print('Problem 5')
num = num.add(5)
print()

## Problem 6
print('Problem 6')
df1 = pd.DataFrame({'TV':[230.1,44.5,17.2,151.5,180.8,8.7,57.5,120.2,8.6],
                    'Radio':[37.8,39.3,45.9,41.3,10.8,48.9,32.8,19.6,2.1],
                    'Newspaper':[69.2,45.1,69.3,58.5,58.4,75,23.5,11.6,1],
                    'Sales':[22.1,10.4,9.3,18.5,12.9,7.2,11.8,13.2,4.8]})
print(df1)
print()

## Problem 7
print('Problem 7')
# a)
filepath = ('/Users/shijizhao/Documents/UCI/Courses/'
            'Deep Learning using TF/Week1/00 kc_house_data.csv')

df2 = pd.read_csv(filepath)

# b)
print(df2.shape)

# c)
print(np.mean(df2['price']))

# d)
df3 = df2.loc[df2['price'] > 500000,:]

print(df3.shape)
print()

## Problem 8
print('Problem 8')
import tensorflow as tf

print(tf.__version__)

