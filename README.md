# Humour-Detection
Humour detection in Yelp reviews
Problem Statement : To utilize the state-of-the-art in deep learning methods and show that deep learning can capture the higher order structure of humor in Yelp reviews, by comparing with state-of-the-art shallow learning techniques. 

#Run :
   Before running make sure all requirements are installed (pip install -r requirements.txt).
   For svm bag-of-words 
	> python svm_bagOfWords.py
   Then on prompt enter in "linear" or "rbf" as per your choice
   
   For Word2Vec & Feed Forward Neural Networks (FFN):
   	Give the output file name of preprocess.py program as input argument to Word2Vec.py in RUN_FFN.sh
	> bash RUN_FFN.sh
