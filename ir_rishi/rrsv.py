from __future__ import division
from itertools import chain,combinations
import operator
import itertools
import glob
import math
import nltk
import pickle
k=3
win=5
def insl(num,lis):
	if len(lis)<k:
		lis.append(num)
	else:
		for a in range(k):
			if num < lis[a]:
				num,lis[a]=lis[a],num
			
	
def aidd(w1,w2,pl):
	if pl[w1]== None or pl[w1]==None:
		return -1
	prodl=[]
	prodl.append(pl[w1])
	prodl.append(pl[w2])
	dlist=[]
	for pair in itertools.product(*prodl):
		if pair[0] < pair [1]:
			x=pair[1]-pair[0]
			if x < win:
				insl(x,dlist)
	if len(dlist)==0:
		return -1
	val=0
	for w in dlist:
		val=val + 1/w
	return val

def 
				
"""		
fp1=open('position list/cf.txt','rb')
cf=pickle.load(fp1)
fp1.close()
f=open("stops.txt","r")
stopworden=f.read()
stopworden=stopworden.split()
fp1=open('position list/collen.txt','rb')
lenc=pickle.load(fp1)
fp1.close()
print 'size of collection is '+str(lenc)
#print("Enter your query")
fp=open("QueryTestSetWithQueryIndex.txt",'r')
queries=fp.readlines()
fp.close()
for query in queries[:250]:
	query=query.split()
	qno=query[0]
	qsb=query[1:]
	q1=[wor.lower() for wor in qsb ]
	print 'for '+ str(qno)
	i=0
	fp=open('./queryResults/query_gId_'+str(qno)+'_top_50.txt')
	files=fp.readlines()
	fp.close()
	files=[(a.split("\\"))[2] for a in files]
	for file in files:
		fp1=open('position list/len_'+file[:-2])
		lend=pickle.load(fp1)
		fp1.close()
		f3=0
		p1=0
		txt=file[:-2]
		fp1=open('position list/df_'+file[:-2],'rb')
		df=pickle.load(fp1)
		fp1.close()
		aidd={}
		fp1=open('position list/poslist_'+file[:-2],'rb')
		poslist=pickle.load(fp1)
		fp1.close()	
	"""	
			
