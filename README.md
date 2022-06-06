# Sentimel-Analysis

My project idea is the text Analysis. 
Sentiment Analysis is the process of determining whether a piece of writing is positive, negative, or neutral.
According to my research, there are certain steps that I need to go through in this project.

      -Collection of the data: analysis of the information that has been collected. 
      -Tokenization: divide the data into chunks or slides 
      -Cleaning the data: remove any type of special characters or punctuation.
      -Remove stop words:  In this step, I will remove any words that don’t add any value to the message. That includes articles or verbs that don’t add meaning to the
feedback.
      -Vectorization process: at this point, all the data used is known by the user. Machines cannot understand words and characters. 
In this step, I will convert the text into numbers to be understood by the machine. 
      -Classification: Determine positive or negative based on a list that checks words and adds punctuation to determine whether the message is positive or negative.

The data suggested in this project are the dialogues of StarWars scripts. 
I will determine the following:
      -	The most active 
      -	The most talkative 
      -	Frequent words 
      -	Positive or negative words in each episode 


*In this project, I am trying to follow the  https://spacy.io/usage/linguistic-features site
and this course on YouTube that introduce me to spacy https://www.youtube.com/watch?v=dIUTsFT2MeQ 


FT1:
During this time, I accomplished the following:

-	Understand the NLP process using the Spacy library 
-	Tokenization 
-	Remove stop words, punctuations, empty spaces as well as new lines(\n).
- Vectorization process  ( Still in process ) 


Using Spyder, I installed the spacy library using the command line: 
      -	pip install -U spacy 
      -	conda install -c conda-forge spacy
Either one will work 
Then, I import the library into my (.py) file. 
1)	Obtain data 
I have implemented a function that will return the three files. These files will be converted into an NLP file that allows me to implement the different 
attributes for tokenization. 
2)	Tokenization : I implement different token attributes to obtain some of the information needed from the dataset and clean the data 
          i.	.text
          ii.	Lemma_
          iii.	Post_
          iv.	Is_stop
          v.	Is_punct 
3)	Classification - Vectorization 
 				Still in Process  





