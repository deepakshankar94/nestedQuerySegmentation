from __future__ import division
import nltk
import glob
import math
import operator
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
    if c==0:
        return 1
    else:
        p=P(c,lc)
        x=200*p
        y=t/x
        k=1+y
        m=math.log10(k)
        return m
def kld2(ld):
    z=200+ld
    l=200/z
    z2=math.log10(l)
    return z2
def kldcal(w,D,C,lc,ld):
    f3=0
    tf1=tf(w,D)
    cf1=cf(w,C)
    f1=kld1(tf1,cf1,lc)
    f2=kld2(ld)
    f4=f1+f2
    return f4
docs=" "
cols=" "
l1=[]
print 'collecting data from database'
fp=open('collection.txt','r')
colfiles=fp.readlines()
for file in colfiles:
    f=open('./Document Collection/'+file[:-2])
    cols=cols+f.read()
    f.close()
l1=nltk.word_tokenize(cols)
lenc=len(l1)
print 'done making collection'
print lenc
#print("Enter your query")
fp=open("QueryTestSetWithQueryIndex.txt",'r')
queries=fp.readlines()
fp.close()
print 'calculating kld values'
for query in queries:
	query=query.split()
	qno=query[0]
	qsb=query[1:]
	q1=[wor.lower() for wor in qsb ]
	print 'for query '+qno 
	form={}
	l2=[]
	i=0
	fp=open('./queryResults/query_gId_'+qno+'_top_50.txt')
	files=fp.readlines()
	fp.close()
	files=[(a.split("\\"))[2] for a in files]
	for file in files:
	    f=open('./Document Collection/'+file[:-2])
	    i=i+1
	    txt=file[:-2]
	    docs=f.read()
	    l2=nltk.word_tokenize(docs)
	    lend=len(l2)
	    f3=0
	    for w in q1:
	        f3=f3+kldcal(w,l2,l1,lenc,lend)
	    form[txt]=f3
	fp=open('./kld/query_gId_'+qno+'_top_50.txt','w')
	for url in form.keys():
		fp.write(url+" "+str(form[url])+"\n")
