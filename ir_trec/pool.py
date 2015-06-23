from __future__ import division
from math import log
import glob
import operator
import pickle

count=0
fp=open("qno.list",'rb')
qnums=pickle.load(fp)
fp.close()
fc=open('poolcount.txt','w')
for qn in qnums:
	f=open('./queryResults/'+qn+'.txt')
	lines=f.readlines()
	f.close()
	count=0
	#print 'for'+fil
	val={}
	filerank ={}
	fw=open('./pool/'+qn+'.txt','w')
	fw.write(lines[0])
	for line in lines[1:]:
		linesplit=line.split()
		if linesplit[-1]!='-':
			fw.write(line)
			count+=1
	fc.write(str(count)+'\n')
	
	
