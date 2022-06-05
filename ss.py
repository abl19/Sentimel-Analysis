# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 23:18:45 2022

@author: loren
"""

import nltk 

# Step 1  -- Obtain the data 
"""input_file=input("Type the name of the file: ")
while True:
    try:
        file_1=open(input_file,'r')
        break
    except FileNotFoundError:
        print('The file name is not found')
        input_file=input("Specify the correct file name")
    except IOError:
        print('The file error')
        input_file=input("Specify the correct file name")
"""
# Step 2 - Tokenize the data 
#from nltk.tokenize import sent_tokenize  # Library used for tokenize 
#nltk.download('stopwords')
# Step 3 - Clean the data 
import string 
string1="!@##$$$/*--ddd ddd ddd"
for char in string.punctuation:
    a_string=string1.replace(char,"")
print(a_string)

##for i in  string1:
  #  list_1=i.split()
   # print(list_1)
    

# Step 3 - Remove Stop words 
from nltk.corpus import stopwords
stopwords=stopwords.words('english')

list_1=[]




# Step 4 - Classification of the words 

   