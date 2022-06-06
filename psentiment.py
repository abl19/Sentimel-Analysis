# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:51:31 2022
@author: loren
"""
from textblob import TextBlob
import pandas as pd
import numpy as np
from keras import regularizers, optimizers
from keras.layers import Embedding, Dense, Dropout, Input, LSTM, GlobalMaxPool1D
from keras.models import Sequential
from keras.initializers import Constant
from tensorflow import keras
import spacy
from collections import Counter

#Vectorizer = TextVectorization()

# Function that will read all three files,close it and return it the store variables 
def reading_files():
    with open(file='SW_EpisodeIV.txt',mode='r',encoding='utf-8') as file:
        file_1=file.read()
    with open(file='SW_EpisodeV.txt',mode='r',encoding='utf-8') as file:
        file_2=file.read()
    with open(file='SW_EpisodeVI.txt',mode='r',encoding='utf-8') as file:
        file_3=file.read()
    return file_1,file_2,file_3
# Clean the data and obtain the Token, Lemma 
def clean_data(file):
    newlist=[]
    characters=[]  # List of Characters 
    for token in file:
        print(token.sen)
        #Process of removing any ing, past verb to gerund or base for  / Removing Stop Words and Puncth
        if token.is_stop!=True and token.is_punct!=True:
            if token.text!=" " and token.text!="\n" and  token.is_digit!=True:
                newlist.append(tuple([token.lemma_.lower()]))  
                if token.pos_=='PROPN':
                    if token.text  in characters:
                        continue
                    else:
                        characters.append(token.text.lower())
    #print(characters)
    return newlist
nlp = spacy.load('en_core_web_lg')
# Files 
file_1,file_2,file_3=reading_files()
file_1=nlp(file_1)
# clean
file1_clean=clean_data(file_1)
# Obtain the most common word 




