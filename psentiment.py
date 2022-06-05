# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:51:31 2022
@author: loren
"""
import spacy
# import pandas as pd 
 
# Function that will read all three files,close it and return it the store variables 
def reading_files():
    with open(file='SW_EpisodeIV.txt',mode='r',encoding='utf-8') as file:
        file_1=file.read()
    with open(file='SW_EpisodeV.txt',mode='r',encoding='utf-8') as file:
        file_2=file.read()
    with open(file='SW_EpisodeVI.txt',mode='r',encoding='utf-8') as file:
        file_3=file.read()
    return file_1,file_2,file_3
nlp = spacy.load('en_core_web_lg')
# Files 
file_1,file_2,file_3=reading_files()
#Step 1 -- Cleaning the data Tokenization  Process 
#1. Obtaining Tokens 
file_1=nlp(file_1)
for token in file_1:
    print(token.text,token.pos_,token.dep_)
    #Process of removing any ing, past verb to gerund or base for
    if not token.is_stop and not token.is_punct: #2. Removing Stop Words and Puncth
        clean_filter=token.lemma_
        print(token.text,token.pos_,token.dep_)
       #print(token,clean_filter)