#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import sklearn
from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

d = []

def create_tfidf_training_data(docs):
	y = [d[0] for d in docs]
	corpus = [d[1] for d in docs]
	vectorizer = TfidfVectorizer(min_df = 1)
	X = vectorizer.fit_transform(corpus)
	return X, y

def train_svm(X, y, k):
	if k == 'linear':
		svm = SVC(C=1.0, kernel='linear')
	elif k =='rbf':
		svm = SVC(C=1.0, kernel='rbf')
	svm.fit(X, y)
	return svm


if __name__ == "__main__":

	k = raw_input("Enter kernel type (linear/rbf):")
	
	#creating Bag-of-words features
	print "creating tfidf features..."
	dataFile = open('data.txt','rb')
	d = pickle.load(dataFile)
	X, y = create_tfidf_training_data(d)

	#separating training and testing data
	print "spliting into train, test data..."
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state = 42)

	#training classifier
	print"training..."
	svm = train_svm(X_train, y_train, k)

	#save classifier for future use if required
	clf = open('clf.txt','w')
	pickle.dump(svm, clf)

	print "prediction results on test data..."
	predictions = svm.predict(X_test)

	#print(svm.score(X_test, y_test))
	print "Accuracy: ",
	print accuracy_score(y_test, predictions)

	dataFile.close()
