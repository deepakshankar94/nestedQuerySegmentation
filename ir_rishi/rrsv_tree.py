from __future__ import division
from itertools import chain,combinations
import operator
import itertools
import glob
import math
from nltk.tree import Tree
import pickle
k=3
win=5
delt=4
wrank=10
def insl(num,lis):
	if len(lis)<k:
		lis.append(num)
	else:
		for a in range(k):
			if num < lis[a]:
				num,lis[a]=lis[a],num
			
	
def aidd(w1,w2,pl):
	if pl[w1]== None or pl[w2]==None:
		return 0
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
		return 0
	val=0
	for w in dlist:
		val=val + 1/w
	return val

"""def treedist(w1,w2,tr):
	sub=[]
	for a in tr:
		sub.append(a)	
	if len(sub)==0:
		if w1==tr.__str__()[1:-2] or w2==tr.__str__()[1:-2]:
			return (1,1)
		else:
			return (0,0)
	elif len(sub)==2:
		(l,lx)=treedist(w1,w2,sub[0])
		(r,rx)=treedist(w1,w2,sub[1])
		if max(lx,rx)==2:
			return (max(l,r),2)
		if lx ==1 and rx ==1 :
			return (l+r,2)
		elif lx ==0 and rx ==0:
			return (max(l,r),0)
		else:
			return (max(l,r)+1,1)
	elif len(sub)==3:
		(l,lx)=treedist(w1,w2,sub[0])
		(m,mx)=treedist(w1,w2,sub[1])
		(r,rx)=treedist(w1,w2,sub[2])
		if max(mx,lx,rx)==2:
			return (max(l,m,r),2)
		if mx==0:
			if lx ==1 and rx ==1 :
				return (l+r,2)
			elif lx ==0 and rx ==0:
				return (max(l,r,m),0)
			else:
				return (max(l,r)+1,1)
		elif mx==1:
			if lx ==1 or rx ==1 :
				return (m+max(l,r),2)
			elif lx ==0 and rx ==0:
				return (m+1,1)
			else:
				print 'whaaaat'
				return (max(l,r)+1,1)
	else:
		print 'gsergsegrsrg'	
"""		
def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    pos1=0
    pos2=1
    for x in numbers:
        if x[1] > m2:
            if x[1] >= m1:
                m1, m2 = x[1], m1 
                pos1,pos2=count,pos1          
            else:
                m2 = x[1]
                pos2=count
        count += 1
    return (m1,m2,pos1,pos2) if count >= 2 else None
def treedist(w1,w2,tr):
	sub=[]
	res=[]
	for a in tr:
		sub.append(a)
		res.append(treedist(w1,w2,a))	
	if len(sub)==0:
		if w1==tr.node or w2==tr.node:
			return (1,1)
		else:
			return (0,0)
	mx,sx,pos1,pos2=second_largest(res)
	if mx==2:
		return (res[pos1][0],2)
	elif mx == 1 and sx==1:
		return (res[pos1][0]+res[pos2][0],2)
	elif mx ==1 and sx == 0 :
		return (res[pos1][0]+1,1)
	elif mx == 0 and sx ==0:
		return (0,0)
	else:
		print 'whaaat' 
def tag(tr):
	global coun1
	if tr.node == '':
		for xtree in tr:
			tag(xtree)
	else:
		tr.node = tr.node + str(coun1)
		coun1=coun1+1

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
rrsv={}
fp1=open('./Nested/scheme_016_S_OP_J_CD.txt','r')
nesqueries=fp1.readlines()
fp1.close()
for num in range(250):
	query=queries[num]
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
	rrsvfil={}
	coun1=1
	atree=Tree(nesqueries[num])
	tag(atree)
	qsbtag=[]
	coun1=1
	for xtag in qsb:
		qsbtag.append(xtag+str(coun1))
		coun1=coun1+1
	for file in files:
		fp1=open('position list/len_'+file[:-2])
		lend=pickle.load(fp1)
		fp1.close()
		txt=file[:-2]
		fp1=open('position list/df_'+file[:-2],'rb')
		df=pickle.load(fp1)
		fp1.close()
		fp1=open('position list/poslist_'+file[:-2],'rb')
		poslist=pickle.load(fp1)
		fp1.close()
		a=0	
		for fw in range(len(qsb)):
			for sw in range(fw+1,len(qsb)):
				td,zx=treedist(qsbtag[fw],qsbtag[sw],atree)
				if zx!=2:
					print zx
				if td<delt:
					a=a+(aidd(qsb[fw],qsb[sw],poslist)/td)
		rrsv[' '.join(qsb)+txt]=a
		rrsvfil[txt]=a
	meth_final=sorted(rrsvfil.items(),key=operator.itemgetter(1),reverse=True)
	flis={}
	rank=1
	for val in meth_final:
		flis[val[0]]=rank
		rank=rank+1
	sav={}
	for i in range(len(files)):
		filc=files[i][:-2]
		sav[filc]=(wrank/(flis[filc]+1))+1/(i+1+1)
	finalr=sorted(sav.items(),key=operator.itemgetter(1),reverse=True)
		
		
	top_no=[5,10,20,50]
				
	for num in top_no:
			fp=open('./results/query_'+str(qno)+'_result_nestedr_top_'+str(num)+'.txt','w')
			fp.write(" ".join(qsb)+'\n')
			for pair in finalr[:num]:
				fp.write(str(pair[0]).split('C')[0]+" "+str(pair[1])+"\n")
				
			fp.close()	
f=open('rrsvnested','wb')
pickle.dump(rrsv,f)
f.close()					
		
			
