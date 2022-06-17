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
                                         
![Figure 2022-06-16 232433 (3)](https://user-images.githubusercontent.com/106505515/174218728-35d3ff4d-3824-4560-8fb9-2730a28300f7.png)
![Figure 2022-06-16 232433 (4)](https://user-images.githubusercontent.com/106505515/174218729-0f92d063-d50f-45b4-b362-6b7ed0ba1bc6.png)
![Figure 2022-06-16 232433 (5)](https://user-images.githubusercontent.com/106505515/174218731-8d81babd-0269-4681-a060-40c3e7042a41.png)


                                                Common Words per Episode
                                    
![Figure 2022-06-16 232433 (0)](https://user-images.githubusercontent.com/106505515/174218725-85ab6f5d-b1cf-42f0-9dcd-47b4cdd3534b.png)
![Figure 2022-06-16 232433 (1)](https://user-images.githubusercontent.com/106505515/174218726-b257f8cd-d4ad-41d3-bf53-0c8f5b563098.png)
![Figure 2022-06-16 232433 (2)](https://user-images.githubusercontent.com/106505515/174218727-d288a301-0420-4a30-af74-4907b4a69240.png)

                                 



