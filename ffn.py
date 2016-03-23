import gensim
import numpy
import codecs
import logging
import sys
import nltk
import pickle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import SoftmaxLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
reload(sys)

sys.setdefaultencoding('utf-8')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = gensim.models.word2vec.Word2Vec.load('Yelp_Reviews')
reviewLst = []

def readFileOfReviews():
# Read each review from file
        global reviewLst
        preview = open("data.txt", "rb")
        reviewLst =  pickle.load(preview)


def createTrainingList(reviewLst):
    sds = SupervisedDataSet(100,1)
    for review in reviewLst:
        revString = unicode(review[1], errors='ignore')
        revSentences = nltk.word_tokenize(revString.strip())
        revWords = []
        for i in revSentences:
            revWords += i.lower().split()
        vec = 0
        for i in revWords:
            try:
                vec+=model[i]
            except:
                pass
        vec=vec/len(revWords)
        sds.addSample(vec,review[0])
    net = buildNetwork(100, 20, 1, hiddenclass=TanhLayer, outclass=SoftmaxLayer,bias=True)
    trainer = BackpropTrainer(net, sds)
    print "Score1:",trainer.train()
    print "Score2:",trainer.trainUntilConvergence(verbose=True,maxEpochs=100)

readFileOfReviews()
createTrainingList(reviewLst)
"""ds = SupervisedDataSet(100, 2)
for i in range(0,25001):
    ds.addSample(tuple(model1.docvecs[i]),(1,0))
print "Dataset length:",len(ds)
print "Dataset built"
print "Building Network"


print "Network Built"
print "Backpropogation Completed"

print "After Convergence:"
"""
