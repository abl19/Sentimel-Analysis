import pandas as pd
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import os
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
from collections import OrderedDict, defaultdict, Counter
import pandas as pd
import csv
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import CountVectorizer
import tokenize
from nltk.tokenize import word_tokenize
from tokenize import tokenize
import itertools
from PIL import Image
from wordcloud import WordCloud

# Function that will read all three files,close it and return it the store variables 
def reading_files():
    with open(file='SW_EpisodeIV.txt',mode='r',encoding='utf-8') as file:
        file_1=file.read()
    with open(file='SW_EpisodeV.txt',mode='r',encoding='utf-8') as file:
        file_2=file.read()
    with open(file='SW_EpisodeVI.txt',mode='r',encoding='utf-8') as file:
        file_3=file.read()
    return file_1,file_2,file_3

# Text transformations
def cleancorpus(txtfile):
    stop_words = set(stopwords.words('english'))
    # add words that aren't in the NLTK stopwords list
    new_stopwords = ['thats','weve','hes','theres','ive','im','will','can','cant','dont','youve','us'
        ,'youre','youll','theyre','whats','didnt']
    new_stopwords_list = stop_words.union(new_stopwords)
    data1 = pd.read_csv(txtfile, delimiter='|')
    pd.set_option('max_colwidth', 200)
    data1["dialogue"] = data1["dialogue"].str.replace('[^\w\s]','')
    data1.dialogue = data1.dialogue.apply(lambda x: x.lower())
    data1.dialogue = data1.dialogue.str.replace('\d+', '')
    data1.dialogue = data1.dialogue.str.split().apply\
        (lambda x: ' '.join(item for item in x if item not in new_stopwords_list))
    data1.dialogue = data1.dialogue.str.replace('  ', '')
    #print(data1.dialogue.head(120))
    #print(data.dialogue)
    return data1
def get_top_n_words(corpus):
    word_list = []
    dialogue_list = pd.Series(corpus['dialogue'])
    dialogue_list_temp = dialogue_list.tolist()
    for stat in dialogue_list_temp:
        word_list.extend(stat.split())
    word_series = pd.Series(word_list)
    return word_series.value_counts()
def most_frequent_bigrams(freq_bigrams):
    bigrams_list = pd.Series(freq_bigrams)
    count_bigrams = bigrams_list.value_counts().head(20)
    return count_bigrams
def seriestodf(series):
    df_temp = pd.DataFrame(series)
    df_temp.reset_index(inplace=True)
    df_temp.columns = ('Character', 'Dialogue')
    return df_temp
def seriestodfbigram(series):
    df_temp = pd.DataFrame(series)
    df_temp.reset_index(inplace=True)
    df_temp.columns = ('Bigram', 'Frequency')
    return df_temp
def bigrams_calculate(bigramfile):
    i = cleancorpus(bigramfile).dialogue \
        .str.split(expand=True) \
        .stack()
    j = i + ' ' + i.shift(-1)
    bigrams = j.dropna().reset_index(drop=True)
    return bigrams

def ggplt(df_ep):
    plt.style.use('ggplot')
    ax = df_ep[['Character', 'Dialogue']].plot(kind='bar', title="Dialogues by a character(Top 20)", figsize=(15, 10),
                                               legend=True, fontsize=12)
    ax.set_xlabel("Character", fontsize=12)
    ax.set_ylabel("Number of Dialogues", fontsize=12)
    return plt.show()
def wordcloud(data_file):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    eiv = (get_top_n_words(cleancorpus(data_file)))
    mask = np.array(Image.open(path.join(d, 'C:\\Users\\kahma\\Downloads\\star-wars-movie-scripts'
                                        '\\star-wars-movie-scripts\\wordcloud_masks\\yoda.png')))
    eiv_wc = WordCloud(width=1000, height=1000, background_color='white', mask=mask, random_state=21,
                   max_font_size=110).generate(str(eiv))
    fig = plt.figure(figsize=(32, 16))
    plt.imshow(eiv_wc)
    
file_1,file_2,file_3=reading_files()
Top20Chars_ep4 = cleancorpus(file_1).character.value_counts().head(20)
df_ep4_bigram = seriestodfbigram(most_frequent_bigrams(bigrams_calculate(file_1)))
#print(Top20Chars_ep4)
df_ep4 = seriestodf(Top20Chars_ep4)
ggplt(df_ep4)
wordcloud(file_1)