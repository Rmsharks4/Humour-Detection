# Humour-Detection
Humour detection in Yelp reviews

####Problem Statement : 
To utilize the state-of-the-art in deep learning methods and show that deep learning can capture the higher order structure of humor in Yelp reviews, by comparing with state-of-the-art shallow learning techniques. 

###Applications :
Humor is a necessary part of all verbal communication. With the advancement of computational technologies, increasingly more emphasis is being placed on systems that can handle human natural language effectively. Thus, without humor detection and generation, no natural language system can be considered successful. It is necessary for a full computational understanding of natural language documents and for enabling intelligent conversational agents to handle humor.

Domain specific application: Yelp is a platform which aims to provide accurate, crowd-sourced opinion about a place of business. Humour detection in the reviews present there, can be used to determine the importance, or the genuineness of a particular review.

###Challenges
- Any results derived from work on Yelp data may end up being highly domain specific. But, the lack of any openly available dataset for humour leaves no option.
- The human classification of something as “humour” can be very subjective.

###Dataset:
We are using the  Yelp Dataset Challenge dataset, which consists of about 1.6 million reviews by 366,000 users for 61,000 businesses. Each yelp review has user given votes for three categories - “funny”, “cool” and “useful”.  We are using this community provided data to get our dataset. Any review with more than 3 “funny votes” is taken as funny, and the others as not-funny. We extracted a balanced set of 1,00,000 reviews, containing equal number of samples for both classes. This data is be used for training and testing purposes for this project.


###Modules:
1. SVM on bag-of-words word representations, 5-fold cross validation
  * Linear kernel
  * RBF Kernel
2. Feed Forward Network on word2vec generated word vectors
3. Convulational Neural Networks

###Run:

   Before running make sure all requirements are installed 

     > pip install -r requirements.txt


1. For SVM built on top of bag-of-words word representations 
	   
       > python svm_bagOfWords.py

   Then on prompt enter either "linear" or "rbf" as per your choice
   
2. Feed Forward Neural Networks (FFN) built on top of word2vec genrated word vectors:

   	Give the output file name of preprocess.py program as input argument to Word2Vec.py in RUN_FFN.sh
	> bash RUN_FFN.sh

3. Convulational neural networks:

    The code given in Yoon Kim's code for [CNN for sentence classification](https://github.com/yoonkim/CNN_sentence) was used. The pre-trained [Google's news corpus](https://code.google.com/archive/p/word2vec/) word vector representations are used.

###Results:
Accuracy scores achieved were as follows:

1. SVM
  - Linear Kernel: 0.83
  - RBF kernel: 0.497

2. Feed Forward Neural Network:  0.75

2. Convolutional Neural Network
  - Static: 
    - word2vec: 0.8015
    - random: 0.754
  - Non-static:
    - word2vec: 0.8073
    - random: 0.7831

###Links:
1. [Project webpage](http://srishti-1795.github.io/Humour-Detection/)
2. [Youtube Video](https://youtu.be/Y2VHCbGppMs)
3. [Presentation](http://www.slideshare.net/SrishtiAggarwal5/humour-detection)

###References:
- [Oliveira and Rodrigo, "Humor Detection in Yelp reviews" ](https://cs224d.stanford.edu/reports/OliveiraLuke.pdf)
- [Yoon Kim, "Convolutional Neural Networks for Sentence Classification"](http://emnlp2014.org/papers/pdf/EMNLP2014181.pdf)
