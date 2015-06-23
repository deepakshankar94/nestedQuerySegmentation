from __future__ import division
from itertools import chain,combinations
import operator
import itertools
import glob
import math
import nltk
import pickle
mu=1
def tfm(l,pl,name,que):
    global tfmstore
    return tfmstore[" ".join(que)+" ".join(l)+name]
def tf(w,doc):
    t=0
    for words in doc:
        if w == words:
            t=t+1
    return t

def cf(w,coll):
    c=0
    for words in coll:
        if w == words:
            c=c+1
    return c

def P(c,lc):
    return(c/lc)


def kld1(t,c,lc):
    global mu
    if c==0:
        return 1
    else:
        p=P(c,lc)
        x=mu*p
        y=t/x
        k=1+y
        m=math.log10(k)
        return m
def kld2(ld):
    global mu
    z=mu+ld
    l=mu/z
    z2=math.log10(l)
    return z2
def kldcal(w,df1,cf1,lc,ld):
    
    f1=kld1(df1,cf1,lc)
    f2=kld2(ld)
    f4=f1+f2
    return f4

def prox(l,t,cf1,lc):
	proxval=0
	global mu
	for word in l:
		if cf1[word]==0:
			proxval+=1
    	else:
    	    p=P(cf1[word],lc)
    	    x=mu*p
    	    y=t/x
    	    k=1+y
    	    proxval+=math.log10(k)
	return proxval        

fp1=open('position list/cf.txt','rb')
cf=pickle.load(fp1)
fp1.close()
f=open('tfm.txt','rb')
tfmstore=pickle.load(f)
f.close()
f=open("stops.txt","r")
stopworden=f.read()
stopworden=stopworden.split()
fp1=open('position list/collen.txt','rb')
lenc=pickle.load(fp1)
fp1.close()
print 'size of collection is '+str(lenc)
fmain=open('kldall.txt','w')
#print("Enter your query")
fp=open("QueryTestSetWithQueryIndex.txt",'r')
queries=fp.readlines()
fp.close()
for query in queries[0:250]:
	query=query.split()
	qno=query[0]
	qsb=query[1:]
	q1=[wor.lower() for wor in qsb ]
	form={}
	l2=[]
	print 'for '+ str(qno)
	i=0
	#df={}
	proxicpe={}
	proxicpes={}
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
		fp1=open('position list/poslist_'+file[:-2],'rb')
		poslist=pickle.load(fp1)
		fp1.close()	
		for w in q1:
			f3=f3+kldcal(w,df[w],cf[w],lenc,lend)
		form[txt]=f3
		fpc=open('./cpe/'+str(qno)+'_cpe')
		correct=fpc.readlines()
		fpc.close()
		#print 'for cpe'
		missed=[]
		for wor in correct:
			l=wor.split()
			tfprox=tfm(l,poslist,file[:-2],qsb)
			p1=p1+prox(l,tfprox,cf,lenc)
		proxicpe[txt]=p1
		p1=0
		fpc=open('./cpes/'+str(qno)+'_cpes')																																																																				
		correct=fpc.readlines()
		fpc.close()
		#print 'for cpes'
		for wor in correct:
			l=wor.split()
			tfprox=tfm(l,poslist,file[:-2],qsb)
			p1=p1+prox(l,tfprox,cf,lenc)
		proxicpes[txt]=p1
	qlen=len(qsb)
	for url in form.keys():
		proxicpe[url]=proxicpe[url]/qlen+form[url]
		proxicpes[url]=proxicpes[url]/qlen+form[url]
	meth_final={}
	meth_final['kld']=sorted(form.items(),key=operator.itemgetter(1),reverse=True)
	meth_final['cpe']=sorted(proxicpe.items(),key=operator.itemgetter(1),reverse=True)
	meth_final['cpes']=sorted(proxicpes.items(),key=operator.itemgetter(1),reverse=True)
	methods=['kld','cpe','cpes']
	top_no=[5,10,20,50]
	for meth in methods:
		for num in top_no:
			fp=open('./results/query_'+str(qno)+'_result_'+meth+'_top_'+str(num)+'.txt','w')
			fp.write(" ".join(qsb)+'\n')
			for pair in meth_final[meth][:num]:
				fp.write(str(pair[0]).split('C')[0]+" "+str(pair[1])+"\n")
			fp.close()


