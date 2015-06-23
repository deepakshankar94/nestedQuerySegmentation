from itertools import chain,combinations
from __future__ import division
import nltk
import operator
import itertools
from nltk.corpus import stopwords
import glob
import math



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
		
docs=""
cols=""
l1=[]
fp=open('collection.txt','r')
colfiles=fp.readlines()
for file in colfiles:
    f=open('./Document Collection/'+file[:-2])
    cols=cols+f.read()
    f.close()
l1=nltk.word_tokenize(cols)
l1=[wor.lower() for wor in l1 ]
lenc=len(l1)
i=0
df={}
proxi={}
for file in glob.glob('C:/text/*'):
    f=open(file)
    i=i+1
    txt="text-%d"%i
    docs=f.read()
    l2=nltk.word_tokenize(docs)
    l2=[wor.lower() for wor in l2]
    lend=len(l2)
    df=indexing(qsb,l2)
    p1=0
    for wor in correct:
        l=([x[0] for x in wor])
        tf=tfm(l,df)
        cf1=cf(l,l1)
        p1=p1+prox(tf,cf1,lenc)
    proxi[txt]=p1
print(sorted(proxi.items(),key=operator.itemgetter(1),reverse=True))       
