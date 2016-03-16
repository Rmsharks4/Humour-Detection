#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pickle

d = []

def getData(inputFile, dataFile):
	funnyCount = 0
	notFunnyCount = 0

	for line in inputFile:
		data = json.loads(line)
		if data["votes"]["funny"] > 2 and funnyCount < 50000:
			funnyCount += 1
			t = ('1',data["text"].encode('utf-8'))
			d.append(t)

		elif notFunnyCount< 50000:
			notFunnyCount += 1
			t = ('0',data["text"].encode('utf-8'))
			d.append(t)

		else:
			if funnyCount >= 50000 and notFunnyCount >= 50000:
				break

	print len(d)
	pickle.dump(d, dataFile)
	
	return d

if __name__ == "__main__":

	inputFile = open('dataset/yelp_academic_dataset_review.json','r')
	dataFile = open('data.txt','w')

	getData(inputFile, dataFile)

	inputFile.close()
	dataFile.close()

	# dataFile = open('data.txt','r')
	# x = pickle.load(dataFile)
	# print x
	# dataFile.close()


