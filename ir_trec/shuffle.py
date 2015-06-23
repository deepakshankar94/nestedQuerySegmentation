from __future__ import division
from itertools import chain,combinations
import operator
import itertools
import glob
import math
import nltk
import pickle
from random import shuffle
fp=open("query_clean_list.txt",'r')
queries=fp.readlines()
fp.close()
qno=[]
qsb={}
for query in queries:
	query=query.split()
	qnum=query[0]
	qno.append(qnum)
	qsb[qnum]=query[1:]
f=open('fildict.txt','wb')
pickle.dump(qsb,f)
f.close()
#shuffle(qno)
print len(qno)
f=open('qno.txt','w')
for i in qno:
    f.write(i+'\n')
f.close()
f=open('qno.list','wb')
pickle.dump(qno,f)
f.close()

