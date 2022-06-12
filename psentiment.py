# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:51:31 2022
@author: loren
"""
import pandas as pd
import spacy
import csv 
from collections import Counter
import matplotlib.pyplot as plt
import nltk 
from nltk.corpus import stopwords
import string
from matplotlib import pyplot as plt
import numpy as np

# Function that will read all three files,close it and return it the store variables 
def reading_files():
   data1= pd.read_csv("SW_EpisodeIV.txt",
                     delimiter=r'\s+',
                     on_bad_lines='skip')
   data2= pd.read_csv("SW_EpisodeV.txt",
                     delimiter=r'\s+',
                     on_bad_lines='skip')
   data3= pd.read_csv("SW_EpisodeVI.txt",
                     delimiter=r'\s+',
                     on_bad_lines='skip')
   return data1,data2,data3
# Task 1 : Obtain the person who talks the most in each chapter
#  This will need function: most_talking_person, graph File 
def most_talking_persons(data):
    chracter=[]
    quantity=[]
    for each in data['character']:
         word_counts = Counter(data['character'])
         if each not in chracter:  
             chracter.append(each)
         else: 
             continue
    # The most talking persons 
    #word_counts.most_common(10)
    
def graph_file(data,episode): # Most Talkative
    word_counts = Counter(data['character'])
    graph_data=word_counts.most_common(10)
    df = pd.DataFrame(graph_data,columns=['Chracters','Presence'])
    plt.bar(df['Chracters'],df['Presence'],)
    plt.title('The most talking from '+str(episode), fontsize=14)
    plt.xlabel('Presence', fontsize=14)
    plt.ylabel('Characters', fontsize=14)
    plt.xticks(rotation=70)
    plt.figure(figsize=(12, 6))
    plt.show()

def frequenc_words(data,newlist):
    stop_words=stopwords.words('english')
    # Clean the data 
    for token in data['dialogue']:
        token=token.strip().split()
        for words in token:
            if words!='--':
                words=words.lower()
                words=words.strip()
                words=words.strip(string.punctuation)
                if words !="" and words not in stop_words and len(words)>3:
                    if words in newlist:
                        newlist[words]+=1
                    else:
                        newlist[words]=1
    return newlist
    
def graph_common_words(lista,episode):
    value_key=[]
    for key,val in lista.items():
        value_key.append((val,key))
    value_key.sort(reverse=True)
    value_key1=value_key[:10]
    key_list=[val for val,amount in value_key1]
    values=[amount for val,amount in value_key1]
    plt.title('Word Frequency '+str(episode), fontsize=14)
    plt.xlabel('Amount', fontsize=14)
    plt.ylabel('Words', fontsize=14)
    plt.bar(values,key_list,align='center')
    plt.xticks(rotation=70)
    plt.figure(figsize=(15, 8))
    plt.show()
# Reading Data 
file_1,file_2,file_3=reading_files()
# Words Use the most per episode 
newlist={}
lista=frequenc_words(file_1,newlist)
graph_common_words(lista,"Episode 1")
lista=frequenc_words(file_2,newlist)
graph_common_words(lista,"Episode 2")
lista=frequenc_words(file_3,newlist)
graph_common_words(lista,"Episode 3")

# Actor who speak the most per episode
most_talking_persons(file_1)
graph_file(file_1,"Episode 1")
most_talking_persons(file_2)
graph_file(file_2,"Episode 2")
most_talking_persons(file_3)
graph_file(file_3,"Episode 3")
