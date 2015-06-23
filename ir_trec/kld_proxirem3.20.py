from __future__ import division
from itertools import chain,combinations
import operator
import itertools
import glob
import math
import nltk
import pickle
mu=5
def tfm(l,pl,name,que):
    global tfmstore
    try:
        if tfmstore[" ".join(que)+" ".join(l)+name]!=0:
            return tfmstore[" ".join(que)+" ".join(l)+name]
    except KeyError:
        listo=[]
    #list2=[[] for i in range(0,len(l))]
    global stopworden
    pairs=[]
    olist=[]
    list2=[]
    i=1
    first=1000000
    last=0
    extra=int(20000000**(1.0/len(l)))    #how many extra can be there
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
                        a=a[pos:(pos+extra)]
                        len(a)
                        break
                """for pos in range(len(pl.get(w))-1,0,-1):
                    if pl.get(w)[pos-1]<last:
                        a=a[:pos]
                        print sfsf
                        break"""
                i=i*extra
                list2.append(a)
            else:
                i=i*extra
                list2.append(pl.get(w)[:extra])        
            if(i>20000000):                     #thresold
                fp=open("Skipped.txt",'a')
                print 'kya'
                fp.write(" ".join(que)+'\n'+" ".join(l)+'\n'+name+'\n')
                fp.close()
                tfmstore[" ".join(que)+" ".join(l)+name]=0
                return 0       
    #print l
    #print list2
    #print l
    if len(list2)<2:
    	tfmstore[" ".join(que)+" ".join(l)+name]=0
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
    tfm1=0
    for olen in olist:
        if olen==0:
    	    continue
        tfm1=tfm1+(mlen/olen)
    #print 'done'
    tfmstore[" ".join(que)+" ".join(l)+name]=tfm1
    return tfm1
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
f=open('tfmtrec0new.txt','rb')
tfmstore=pickle.load(f)
f.close()
#tfmstore={}
f=open("stops.txt","r")
stopworden=f.read()
stopworden=stopworden.split()
fp1=open('position list/collen.txt','rb')
lenc=pickle.load(fp1)
fp1.close()
print 'size of collection is '+str(lenc)
#print("Enter your query")
fp=open("qno.list",'rb')
qnums=pickle.load(fp)
fp.close()
f=open('fildict.txt','rb')
querystr=pickle.load(f)
f.close()
for query in qnums:
	qno=query
	qsb=querystr[query]
	q1=[wor.lower() for wor in qsb ]
	form={}
	l2=[]
	print 'for '+ str(qno)
	i=0
	#df={}
	proxicpe={}
	proxicpes={}
	fp=open('./queryResults/'+str(qno)+'.txt')
	files=fp.readlines()
	fp.close()
	files=[a.split()[0] for a in files[1:]]
	for file in files:
		fp1=open('position list/len_'+file+'.txt')
		lend=pickle.load(fp1)
		fp1.close()
		f3=0
		p1=0
		txt=file+'.txt'
		fp1=open('position list/df_'+file+'.txt','rb')
		df=pickle.load(fp1)
		fp1.close()
		fp1=open('position list/poslist_'+file+'.txt','rb')
		poslist=pickle.load(fp1)
		fp1.close()	
		for w in q1:
			f3=f3+kldcal(w,df[w],cf[w],lenc,lend)
		form[txt]=f3
		fpc=open('./cpe/'+str(qno)+'_cpe.txt')
		correct=fpc.readlines()
		fpc.close()
		#print 'for cpe'
		missed=[]
		for wor in correct:
			l=wor.split()
			tfprox=tfm(l,poslist,file+'.txt',qsb)
			p1=p1+prox(l,tfprox,cf,lenc)
		proxicpe[txt]=p1
		p1=0
		fpc=open('./cpes/'+str(qno)+'_cpes.txt')																																																																				
		correct=fpc.readlines()
		fpc.close()
		#print 'for cpes'
		for wor in correct:
			l=wor.split()
			tfprox=tfm(l,poslist,file+'.txt',qsb)
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
	top_no=[5,10,20,50,200]
	for meth in methods:
		for num in top_no:
			fp=open('./results/query_'+str(qno)+'_result_'+meth+'_top_'+str(num)+'.txt','w')
			fp.write(" ".join(qsb)+'\n')
			for pair in meth_final[meth][:num]:
			    fp.write(str(pair[0].split('.')[0])+" "+str(pair[1])+"\n")
			fp.close()
#f=open('tfmtrec0new.txt','wb')
#pickle.dump(tfmstore,f)
#f.close()

