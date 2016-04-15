#!/bin/bash
python CNN/separate.py data.txt #path of data.txt file (o/p file of preprocess.py program)
python CNN/GenerateWord2Vec.py path # path of Google Word2Vec bin file
THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 python CNN/CNN_train.py -static -word2vec
THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 python CNN/CNN_train.py -nonstatic -rand
THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 python CNN/CNN_train.py -nonstatic -word2vec
