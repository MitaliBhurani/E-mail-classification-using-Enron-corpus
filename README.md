# Email-classification

This is my first ever project.
The project is based on classifying e-mails of the Enron corpus into two catagories:
1. Confidential e-mails
2. Normal e-mails

About the dataset: 
The Enron e-mail dataset contains over 600,000 e-mails from 158 users.

Why this dataset?
Enron Corporation was a famous American energy, commodities, services company. Enron scandal, a well-planned accounting fraud, led to the company’s bankruptcy. FERC publicly released e-mails from Enron to investigate its involvement in the scandal.
As far as I know this dataset is the only email dataset publicly available.

Objective:
1. Preparing the text data:
   This involves data preprocessing in the follwing ways:
   a) Removal of stop words
   b) Lemmatization
   c) Removal of punctuation marks and special characters
   d) Converting all the words to lowercase
   
2. Creating word dictionary:
   This involves creating a dictionary of words and their frequency. I have chosen 100 most frequently used words in the 
   dictionary.
   
3. Feature extraction process:
   I will extract word count vector (the feature here) of 100 dimensions for each email of training
   set. Each word count vector will contain the frequency of 100 words in the training file.
   
4. Training the classifier:
   Here, I will be using scikit-learn ML library for training classifiers. It is an open source python ML library.
   I will train two models here namely Naive Bayes classifier and Support Vector Machines (SVM). 
   Once the classifiers are trained, I will check the performance of the models on test-set.
   
I have completed the first two steps and am providing the code for the same. The next two steps are yet to be learnt and finished.
