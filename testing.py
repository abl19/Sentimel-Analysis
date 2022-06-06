# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:37:55 2022

@author: loren
"""
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


with open(file='SW_EpisodeIV.txt',mode='r',encoding='utf-8') as file:
    file_1=file.read()