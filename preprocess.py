#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pickle

d = []

def getData(inputFile, dataFile, n):
	funnyCount = 0
	notFunnyCount = 0

	for line in inputFile:
		data = json.loads(line)
		if data["votes"]["funny"] > 2 and funnyCount < n:
			funnyCount += 1
			t = ('1',data["text"].encode('utf-8'))
			d.append(t)

		elif notFunnyCount < n:
			notFunnyCount += 1
			t = ('0',data["text"].encode('utf-8'))
			d.append(t)

		else:
			if funnyCount >= n and notFunnyCount >= n:
				break

	print len(d)
	pickle.dump(d, dataFile)
	
	return d

if __name__ == "__main__":

	outputFileName = raw_input("output file name:")
	n = raw_input("number of datapoints needed for each class:")

	inputFile = open('dataset/yelp_academic_dataset_review.json','r')
	dataFile = open(outputFileName,'w')

	getData(inputFile, dataFile,n)

	inputFile.close()
	dataFile.close()



