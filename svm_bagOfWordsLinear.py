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

def train_svm(X, y):
	svm = SVC(C=1.0, kernel='linear')
	svm.fit(X, y)
	return svm


if __name__ == "__main__":
	dataFile = open('data.txt','rb')
	d = pickle.load(dataFile)

	X, y = create_tfidf_training_data(d)

	print "tfidf features created..."
	X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state = 42)

	trainData = open('trainData.txt','w')
	testData = open('testData.txt','w')
	trainLabels = open('trainLabels.txt','w')
	testLabels = open('testLabels.txt','w')
	pickle.dump(X_train,trainData)
	pickle.dump(y_train, trainLabels)
	pickle.dump(X_test, testData)
	pickle.dump(y_test, testLabels)
	print "split into train, test data..."

	print"training..."
	svm = train_svm(X_train, y_train)

	clf = open('clf.txt','w')
	pickle.dump(svm, clf)

	print "finished training."
	pred = svm.predict(X_test)

	#print(svm.score(X_test, y_test))
	print accuracy_score(y_test, pred)