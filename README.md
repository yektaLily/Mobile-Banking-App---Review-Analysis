# Project Introduction 

This project is partly for a course (MSE623 Big Data Analytics) at University of Waterloo and partly for my Dissertation on Mobile Banking in Canada. Here are the details of the project: 

1. I selected 5 mobile banking apps (CIBC, TD, RBC, BMO and Scotia), and collected app feature data on each manually (by going to their app page on iOS app store) --- related file is the data file titled `ios_app_features.py` 
2. I conducted some explanatory data analysis from the features data in R --- the code is in file `ios_manualData_analysis.Rmd`
3. I scrapped the iOS App store reviews for the 5 banks above and collected review data --- the related code for each bank is in files: `[bankname]_reviews.py` and `ios_scrp_[bankname].py`, additionally combining into one csv file in `ios_featureData_combined.py`
4. I combined all the reviews into 1 file --- the code is in file `ios_reviewData_combined.py`
5. The dataset is ready at this point. I do some basic data analysis --- the code is in file `ios_dataExplore.Rmd` 

Now that the data is ready, I move on with the project plan: 
1. Do topic modeling to find out the main topics of the reviews (what are people talking about)
2. Do sentiment analysis to find positive, negative and neutral reviews
3. Do topic modeling again for each type of review subset (negative, positive and neutral) 

## CLEANING AND PRE-PROCESSING DATA + FIRST (OVERALL) TOPIC MODELING 
The following procedures are implemented for Data Cleaning, which can be found in the jupyternotebook `TopicModeling_iOS.ipynb`: 

1. Only keep English reviews (remove non-English) --- Task: check before and after number of rows (to see how many got deleted)
2. Turn everything into lower case 
3. Remove stopwords + additional stopwords such as "from" "subject" "reply" "app" "bank" "banking" + names of the banks "CIBC", "TD", "BMO", "RBC", "SCOTIA"
4. Remove punctuation 
5. Lemming/Stemming  

Throughtout this process, several **Variations** of the data are kept: 
1. `reviews` is a list of the original data frame's reviews column where each user review is an entry in the list
2. `reviews_corpus` is a block of text where all reviews are joined together, and everything is lower cased  
3. `tokenized_doc_to_sentences` is the sentence tokenized version of `reviews_corpus`, a list of strings 
4. `tokenized_doc_to_words` is the word tokenized version of `tokenized_doc_to_sentences`, a list of lists where each outer list a review, then the inner lists each correspond to the sentences within the review 

The data cleaning is performed on all variations of the data. Therefore, each 4 types of data that are kept have clean and raw versions. Both types are saved to disk for easier upload later. 

### IMPORTANT FUNCTIONS 

Below are descriptions of functions. At various points, we have employed the help of ChatGPT4 (chat.openai.com). Please look out for the comment indicating start and end of code provided or fixed by AI. 

1. `is_english` detects non-English and English texts. We use this function for data cleaning, as several of the reviews are in languages other than English. 
2. `remove_punc` removes punctuation specifically declared as a regular expression in `punctuation_to_remove` 
3. `generate_dictionary` creates a gensim dictionary and corpus, and saves the dictionary to a matrix model format for easier retrival 
4. `print_top_10_words` prints the top 10 words in a corpus using TF-IDF (weighted)
5. `build_lda_model` builds our topic modeling model based on LDA, allowing for several models with different parameters to be trained for comparison to pick the best model parameters (parameter tuning)
6. `train_models` trains the LDA models and returns a list with all the models 
7. `calculate_preplexity` calculates model perplexity 
8. `calculate_coherence` calculates model coherence 
9. `print_topics` prints the topic modeling results with word weights 
10. `remove_stopwords_from_sentence` removes stopwords from sentences while keeping the sentence structure   
11. `build_model_comparison_table` trains several models, and saves the results of perplexity and coherence in one dataframe for easy comparison 
12. `find_best_model` loops through the dataframe of all models trained and finds minimum perplexity and maximum coherence 
13. `pick_best_model` returns the model parameters that give the best combination perplexity and coherence scores 

## SENTIMENT ANALYSIS 
I classify iOS app store reviews using sentiment analysis into positive, neutral and negative reviews. The result would be separating the original reviews data into 3 separate datasets, and conducting topic modeling on each. The steps to achieve this are as follows: 
The code is in the jupyter notebook `SentimentAnalysis_ios.ipynb`. 

#### Manual data labeling 
1. Calculate the mean score (rating) across dataset  
2. Calculate the standard deviation of the scores/rating across dataset  
3. Calculate and store $\mu + \sigma$ in variables called as “upper_accepted” and “lower_accepted”  
4. Manually label data (add column "man_label" to data), as follows:  
	A. If score/rating > upper_accepted  $\rightarrow$  man_label = positive  
	B. If score < lower_accepted $\rightarrow$ man_label = negative  
	C. If lower_accepted $\leq$  score $\leq$ upper_accepted  $\rightarrow$ man_label = neutral  


#### Sentiment Analysis Labeling 
0. Do cross-validation (train, test, validation) 
1. Use various sentiment analysis tools to label data 
2. Use other classification and clustering algorithms to label data 
3. Find the algorithm/technique with the most accurate results (compared with our manual labeling)
4. Do sanity checks of reading the reviews by authors to make sure the labels created make sense  
5. Save 3 separate datasets, `positive_reviews`, `negative_reviews` and `neutral_reviews` 

## TOPIC MODELING FOR SUBSETS OF ORIGINAL DATA 
Lastly, to find out what people are talking about in negative, positive and neutral reviews - I do topic modeling on the 3 separate datasets generated from the previous step. The code is in `ios_topicModeling_sentimentBased.ipynb` Jupyter notebook file. 

A sneak peak at the summary of results: 
### SUMMARY OF RESULTS 

|N-gram|SENTIMENT|Perplexity|Coherence|# of topics|
|------|---------|----------|---------|-----------|
UNI | NEG | -9.536713 | 0.389507 | 15| 
**BI | NEG | -23.903863 | 0.703511 | 15**| 
*TRI | NEG | -21.000096 | 0.779125 | 7*| 
|------|---------|----------|---------|-----------|
UNI | NEU | -9.076156 | 0.355122 | 15 | 
*BI | NEU | -20.940940 | 0.730719 | 15*| 
**TRI | NEU | -29.120526 | 0.569072 | 15**| 
|------|---------|----------|---------|-----------|
UNI | POS | -9.379102 | 0.371542 | 15 | 
*BI | POS | -23.302686 | 0.724604 | 15* | 
**TRI | POS | -30.647355 | 0.686188 | 13**| 

**BEST NEGATIVE MODEL** 
$$score\_neg\_bigram  = (1 + 23.903863) \times 0.5 + 0.5 \times 0.703511 = 12.803687$$
$$score\_neg\_trigram = (1 + 21.000096) \times 0.5 + 0.5 \times 0.779125 = 11.3896105$$

**BEST NEUTRAL MODEL** 
$$score\_net\_bigram  = (1 + 20.940940) \times 0.5 + 0.5 \times 0.730719 = 11.335830$$
$$score\_net\_trigram = (1 + 29.120526) \times 0.5 + 0.5 \times 0.569072 = 15.344799$$ 


**BEST POSITIVE MODEL** 
$$score\_pos\_bigram  = (1 + 23.302686) \times 0.5 + 0.5 \times 0.724604 = 12.513645$$
$$score\_pos\_trigram = (1 + 30.647355) \times 0.5 + 0.5 \times 0.686188 = 16.1667715$$
 

Therefore the best models are: 

- **For Negative**: `neg_bigram_best_model` bigrams 
- **For Neutral**: `net_trigram_best_model` trigrams 
- **For Positive**: `pos_trigram_best_model` trigrams 




Done. 




