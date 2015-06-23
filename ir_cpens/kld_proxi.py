from __future__ import division
from itertools import chain,combinations
import operator
import itertools
import glob
import math
import nltk

def tfm(l,df):
    listo=[]
    list2=[[] for i in range(0,len(l))]
    i=0
    o=[]
    for w in l:
        list2[i]=df.get(w)
        i=i+1
    #print(list1)
    for elements in itertools.product(*list2):
        listo.append(elements)
    
    sum=0
    for element in listo:
        sum=0
        for i in range(1,len(element)):
            sum+=element[i]
        sum=element[0]-sum
        o.append(sum)
    sum=0
    for w in o:
        sum+=w
    m=len(l)
    m1=m-1
    o1=sum-1
    return(m1/o1)
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
    
def indexing(p,D):
    l=(set(p))
    for w in l:
        l1=[]
        for i in range(0,len(D)):
            if w==D[i]:
                l1.append(i)
        df[w]=l1
    #print(df.items())
    return df

def prox(t,c,lc):
    if c==0:
        return 1
    else:
        p=P(c,lc)
        x=200*p
        y=t/x
        k=1+y
        m=math.log10(k)
        return m        

docs=" "
cols=" "
l1=[]
print 'collecting data from database'
fp=open('collection.txt','r')
colfiles=fp.readlines()
fp.close()
for file in colfiles:
    f=open('./Document Collection/'+file[:-2])
    cols=cols+f.read()
    f.close()
l1=nltk.word_tokenize(cols)
lenc=len(l1)
print 'done making collection'
print 'size of collection is '+str(lenc)
#print("Enter your query")
fp=open("QueryTestSetWithQueryIndex.txt",'r')
queries=fp.readlines()
fp.close()

for query in queries:
	query=query.split()
	qno=query[0]
	qsb=query[1:]
	q1=[wor.lower() for wor in qsb ]
	form={}
	l2=[]
	print 'for '+ str(qno)
	i=0
	df={}
	proxicpe={}
	proxicpes={}
	fp=open('./queryResults/query_gId_'+str(qno)+'_top_50.txt')
	files=fp.readlines()
	fp.close()
	files=[(a.split("\\"))[2] for a in files]
	for file in files:
		f=open('./Document Collection/'+file[:-2])
		i=i+1
		txt=file[:-2]
		docs=f.read()
		f.close()
		l2=nltk.word_tokenize(docs)
		lend=len(l2)
		f3=0
		p1=0
		df=indexing(qsb,l2)
		
		for w in q1:
			f3=f3+kldcal(w,l2,l1,lenc,lend)
		form[txt]=f3
		fpc=open('./cpe/'+str(qno)+'_cpe')
		correct=fpc.readlines()
		fpc.close()
		for wor in correct:
			l=wor.split()
			tfprox=tfm(l,df)
			cf1=cf(l,l1)
			p1=p1+prox(tfprox,cf1,lenc)
		proxicpe[txt]=p1
		p1=0
		fpc=open('./cpes/'+str(qno)+'_cpes')																																																																				
		correct=fpc.readlines()
		fpc.close()
		for wor in correct:
			l=wor.split()
			tfprox=tfm(l,df)
			cf1=cf(l,l1)
			p1=p1+prox(tfprox,cf1,lenc)
		proxicpes[txt]=p1
	qlen=len(qsb)
	for url in form.keys():
		proxicpe[url]=proxicpe[url]/qlen+form[url]
		proxicpes[url]=proxicpes[url]/qlen+form[url]
	meth_final={}
	meth_final['kld']=sorted(form.items(),key=operator.itemgetter(1),reverse=True)
	meth_final['cpe']=sorted(proxicpe.items(),key=operator.itemgetter(1),reverse=True)
	meth_final['cpes']=sorted(proxicpes.items(),key=operator.itemgetter(1),reverse=True)
	#fp=open('./results/query_'+str(qno)+'_result_kld'+'_top_5.txt','w')
	#fp.write(qsb+'\n')
	#for pair in kld_final[:5]:
	#	fp.write(pair[0]+" "+str(pair[1])+"\n")
	#fp.close()
	methods=['kld','cpe','cpes']
	top_no=[5,10,20,50]
	for meth in methods:
		for num in top_no:
			fp=open('./results/query_'+str(qno)+'_result_'+meth+'_top_'+str(num)+'.txt','w')
			fp.write(" ".join(qsb)+'\n')
			for pair in meth_final[meth][:num]:
				fp.write(str(pair[0])+" "+str(pair[1])+"\n")
			fp.close()
