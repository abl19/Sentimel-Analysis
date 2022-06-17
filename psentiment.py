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
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import contractions



stop_words = ["i", "me", "my", "myself","going","like", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "oh","s","yes", "u","us","hey","sir","t","ill", "can", "will", "just", "don", "should", "now"]

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
    df = pd.DataFrame(graph_data,columns=['Chracters','Frequency'])
    plt.bar(df['Chracters'],df['Frequency'],)
    plt.title('The most talking from '+str(episode), fontsize=14)
    plt.xlabel('Characters', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(rotation=70)
    plt.figure(figsize=(12, 6))
    plt.show()

def frequenc_words(data,newlist):
    # Libraries that contains different list with stop words 
    # Spacy 
    sp = spacy.load('en_core_web_sm')
    all_stopwords = sp.Defaults.stop_words
    # NLTK Library 
    stopwords = nltk.corpus.stopwords.words("english")
    wnl = WordNetLemmatizer()
    for token in data['dialogue']:
        # Remove Puntuaction , remove extra spaces
        token_lower=token.lower()
        token_clean_contr=contractions.fix(token_lower)
        token_lemma=wnl.lemmatize(token_clean_contr)
        token_remPuct=token_lemma.translate(str.maketrans("","",string.punctuation))
        token=token_remPuct.strip().split()
        for words in token:
            if words not in stop_words and words not in all_stopwords:
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
    plt.xlabel('Words', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.bar(values,key_list,align='center')
    plt.xticks(rotation=70)
    plt.figure(figsize=(15, 8))
    plt.show()
   
    

def train_classifier(lista):
    emotion_list=[]
    with open('emotions.txt','r') as file:
        for line in file:
            clear_line=line.replace("\n",'').replace(',','').replace("'","").strip()
            word,emotion=clear_line.split(':')
            if word in lista:
                emotion_list.append(emotion)
    return emotion_list
    
def graph_sentiments(emotion,message):
    w=Counter(emotion)
    graph_data=w.most_common(10)
    df = pd.DataFrame(graph_data,columns=['Chracters','Frequency'])
    plt.bar(df['Chracters'],df['Frequency'],)
    plt.title('Sentiment '+str(message), fontsize=14)
    plt.xlabel('Sentiments', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(rotation=70)
    plt.figure(figsize=(12, 6))
    plt.show()
      
# Reading Data 
file_1,file_2,file_3=reading_files()

# Words Use the most per episode 
newlist={}
lista_1=frequenc_words(file_1,newlist)
#graph_common_words(lista_1,"Episode 1")
# Sentiment 
sentiment_1=train_classifier(lista_1)
graph_sentiments(sentiment_1,"Episode 1")


lista_2=frequenc_words(file_2,newlist)
#graph_common_words(lista_2,"Episode 2")
# Sentiment
sentiment_2=train_classifier(lista_2)
graph_sentiments(sentiment_2,"Episode 2")


lista_3=frequenc_words(file_3,newlist)
#graph_common_words(lista_3,"Episode 3")
# Sentiment
sentiment_3=train_classifier(lista_3)
graph_sentiments(sentiment_3,"Episode 3")



# Actor who speak the most per episode
most_talking_persons(file_1)
#graph_file(file_1,"Episode 1")
most_talking_persons(file_2)
#graph_file(file_2,"Episode 2")
most_talking_persons(file_3)
#graph_file(file_3,"Episode 3")



