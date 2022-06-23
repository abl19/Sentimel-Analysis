# Sentimel-Analysis

Sentiment Analysis is the process of determining whether a piece of writing is positive, negative, or neutral.
According to my research, there are certain steps that I need to go through in this project.

      -Collection of the data: analysis of the information that has been collected. 
      -Tokenization: divide the data into chunks or slides 
      -Cleaning the data: remove any type of special characters or punctuation.
      -Remove stop words:  In this step, I will remove any words that don’t add any value to the message.
        That includes articles or verbs that don’t add meaning to the feedback.
          
          Tokenization : I implement different token attributes to obtain some of the information needed from the dataset and clean the data 
          i.	.text
          ii.	Lemma_
          iii.	Post_
          iv.	Is_stop
          v.	Is_punct 
        
      -Vectorization process: at this point, all the data used is known by the user. Machines cannot understand words and characters.  
        In this step, I will convert the text into numbers to be understood by the machine. 
      -Classification: Determine positive or negative based on a list that checks words and adds punctuation 
         to determine whether the message is positive or negative.

The data suggested in this project are the dialogues of StarWars scripts. 
I determine the following from the datasets: 
      -	The most talkative 
      -	Frequent words 
      -	Positive or negative words in each episode 

I used the emotion.txt data set to classify the words. 


                                           Character who speak the most per Episode 
                                     
![Figure 2022-06-16 232842 (3)](https://user-images.githubusercontent.com/106505515/174219267-6cabdb60-2d8e-46aa-9049-5cce1a7622c7.png)
![Figure 2022-06-16 232842 (4)](https://user-images.githubusercontent.com/106505515/174219269-ff74f473-676b-4ef3-90f5-0b874d582b9f.png)
![Figure 2022-06-16 232842 (5)](https://user-images.githubusercontent.com/106505515/174219270-8cabbb5e-0976-4535-a65d-3ba13c6a4d1d.png)

                                                Common Words per Episode
                                    
![Figure 2022-06-16 232842 (0)](https://user-images.githubusercontent.com/106505515/174219264-b0a99886-d7ae-4b6a-aadc-4b6d94524e05.png)
![Figure 2022-06-16 232842 (1)](https://user-images.githubusercontent.com/106505515/174219265-bc05e2a8-cdb7-4925-879d-8d4030a687bc.png)
![Figure 2022-06-16 232842 (2)](https://user-images.githubusercontent.com/106505515/174219266-18770142-f458-4283-a209-7946b945249b.png)

                                 
                                                    Sentiment Per Episode 
                                                   
![Figure 2022-06-17 011611 (1)](https://user-images.githubusercontent.com/106505515/174230019-ae63d0d1-8b82-474e-a9b2-369dc3ec31c4.png)
![Figure 2022-06-17 011611 (2)](https://user-images.githubusercontent.com/106505515/174230020-35230c98-1200-4c9e-988a-74057a147ce5.png)
![Figure 2022-06-17 011611 (0)](https://user-images.githubusercontent.com/106505515/174230021-c96eb3fc-a3e4-41ee-860e-9a8e94d31f52.png)
                                      

**Final Conclusions: **

From the graph of sentiments we can conclude that episode 1 and episode 2 are consisted in the sentiment of happiness. However, the second script episode also showed an increase of negative / sad sentimients that continues in the next episode. 

