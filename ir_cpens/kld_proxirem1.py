from __future__ import division
from itertools import chain,combinations
import operator
import itertools
import glob
import math
import nltk
import pickle
mu=2000
def tfm(l,pl,miss):
    listo=[]
    #list2=[[] for i in range(0,len(l))]
    global stopworden
    pairs=[]
    olist=[]
    list2=[]
    i=1
    first=1000000
    last=0
    a=[]
    for w in l:
        if not(w in stopworden):
            if pl[w]!=None:
                first=min(first,pl[w][0])
                last=max(last,pl[w][-1])
    for w in l:
        if pl.get(w)!=None:
            if w in stopworden:
                a=pl.get(w)
                for pos in range(len(pl.get(w))-1):
                    if(pl.get(w)[pos+1]>first):
                        a=a[pos:]
                        break
                for pos in range(len(pl.get(w))-1,0,-1):
                    if pl.get(w)[pos-1]<last:
                        a=a[:pos]
                        break
                i=i*len(a)
                list2.append(a)
            else:
                i=i*len(pl.get(w))
                list2.append(pl.get(w))        
            if(i>19665494):
                fp=open("Skipped.txt",'a')
                fp.write(" ".join(l)+'\n')
                fp.close()
                return 0       
    #print l
    #print list2
    #print l
    if len(list2)<2:
        return 0
    for elements in itertools.product(*list2):#join
        pairs.append((min(elements),max(elements)))
        #i=i+1
        #print i
    #for element in listo:						#join1
        
    pairs=sorted(pairs)
    pleftf=pairs[0][0]
    prightf=pairs[0][1]
    leftf=pairs[0][0]
    rightf=pairs[0][1]
    for tupl in pairs:
        if (tupl[0]>=leftf and tupl[0] <=rightf): 						#overlap present
            if ((tupl[1]-tupl[0])<(rightf-leftf)):						#check if shorter
                if not(tupl[0]>=pleftf and tupl[0] <=prightf):			#push previous if next one not considered
                    olist.append((prightf-pleftf))
                    #print 'accept'+str(pleftf)+' '+str(prightf)
                prightf=rightf
                pleftf=leftf
                rightf=tupl[1]
                leftf=tupl[0]
                #print str(leftf)+' '+str(rightf)
        else:
             olist.append((rightf-leftf))							#push in olist
             #print 'accept'+str(leftf)+' '+str(rightf)
             rightf=tupl[1]
             leftf=tupl[0]
             prightf=rightf
             pleftf=leftf         
    olist.append((rightf-leftf))
    mlen=len(l)-1
    tfm=0
    for olen in olist:
        if olen==0:
    	    continue
        tfm=tfm+(mlen/olen)
    #print 'done'
    return tfm
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
for query in queries:
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
		print file[:-2]
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
			tfprox=tfm(l,poslist,missed)
			p1=p1+prox(l,tfprox,cf,lenc)
		proxicpe[txt]=p1
		p1=0
		fpc=open('./cpes/'+str(qno)+'_cpes')																																																																				
		correct=fpc.readlines()
		fpc.close()
		#print 'for cpes'
		for wor in correct:
			l=wor.split()
			tfprox=tfm(l,poslist,missed)
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
				fp.write(str(pair[0]).split('C')[0]+" "+str(pair[1])+"\n")
			fp.close()
			
