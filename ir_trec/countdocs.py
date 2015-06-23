from __future__ import division
from itertools import chain,combinations
import operator
import itertools
import glob
import math
import nltk
import pickle
fp=open('qno.list','rb')
qno=pickle.load(fp)
fp.close()
total=0
fp=open('judgedcount.txt','w')
for i in qno:
	fp1=open('queryResults/'+i+'.txt','r')
	x=fp1.readlines();
	print len(x)-1
	fp.write(str(len(x)-1)+'\n')
	total+=len(x)-1
fp.write(str(total/75)+'\n')
