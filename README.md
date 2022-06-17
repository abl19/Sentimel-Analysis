# Sentimel-Analysis

Sentiment Analysis is the process of determining whether a piece of writing is positive, negative, or neutral.
According to my research, there are certain steps that I need to go through in this project.

      -Collection of the data: analysis of the information that has been collected. 
      -Tokenization: divide the data into chunks or slides 
      -Cleaning the data: remove any type of special characters or punctuation.
      -Remove stop words:  In this step, I will remove any words that don’t add any value to the message.
        That includes articles or verbs that don’t add meaning to the feedback.
      -Vectorization process: at this point, all the data used is known by the user. Machines cannot understand words and characters.  
        In this step, I will convert the text into numbers to be understood by the machine. 
      -Classification: Determine positive or negative based on a list that checks words and adds punctuation 
         to determine whether the message is positive or negative.

The data suggested in this project are the dialogues of StarWars scripts. 
I will determine the following:
      -	The most talkative 
      -	Frequent words 
      -	Positive or negative words in each episode 


The most talkative  And Frequent words  Outputs : 


FT1:
During this time, I accomplished the following:

-	Understand the NLP process using the Spacy library 
-	Tokenization 
-	Remove stop words, punctuations, empty spaces as well as new lines(\n).
-     Vectorization process  ( Still in process ) 


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
          
FP2: 

-I have completed the analysis of the character who speaks the most and the graph for each of the files. 
-I am working on improving the common words from each one of the files. 
-I start to develop the training set for the sentiment analysis. 

                                           Character who speak the most per Episode 
                                     
![Figure 2022-06-16 232842 (3)](https://user-images.githubusercontent.com/106505515/174219267-6cabdb60-2d8e-46aa-9049-5cce1a7622c7.png)
![Figure 2022-06-16 232842 (4)](https://user-images.githubusercontent.com/106505515/174219269-ff74f473-676b-4ef3-90f5-0b874d582b9f.png)
![Figure 2022-06-16 232842 (5)](https://user-images.githubusercontent.com/106505515/174219270-8cabbb5e-0976-4535-a65d-3ba13c6a4d1d.png)

                                                Common Words per Episode
                                    
![Figure 2022-06-16 232842 (0)](https://user-images.githubusercontent.com/106505515/174219264-b0a99886-d7ae-4b6a-aadc-4b6d94524e05.png)
![Figure 2022-06-16 232842 (1)](https://user-images.githubusercontent.com/106505515/174219265-bc05e2a8-cdb7-4925-879d-8d4030a687bc.png)
![Figure 2022-06-16 232842 (2)](https://user-images.githubusercontent.com/106505515/174219266-18770142-f458-4283-a209-7946b945249b.png)
                                 



