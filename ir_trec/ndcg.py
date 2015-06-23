from __future__ import division
from math import log
import glob
import operator
import pickle
def idcgcal(rank):
	sortrank=sorted(rank.items(),key=operator.itemgetter(1),reverse=True)
	pos=2
	idcg=0
	idcg=idcg+sortrank[0][1]
	#print sortrank[0][0]+' '+str(sortrank[0][1])
	for rank in sortrank[1:10]:
		idcg=idcg+rank[1]/log(pos,2)
		#print rank[0]+' '+str(rank[1])
		pos=pos+1
	return idcg
def dcgcal(listvals,rank,filen,methn):
	pos=1
	dcg=0
	global count
	global fpmiss	
	for val in listvals:
		try:
			if pos==1:
				dcg=dcg+rank[val.split()[0]]
				pos=pos+1
			else:
				dcg=dcg+rank[val.split()[0]]/log(pos,2)
				pos=pos+1
		except KeyError:
			fpmiss.write(filen+'\n')
			fpmiss.write(methn+'\n')
			fpmiss.write(val.split()[0]+'\n')
			count=count+1
	return dcg
count=0
methods=['kld','cpe','cpes']
fpmiss=open('missing_ndcg.txt','w')
fmain=open('kldall.txt','w')
fp=open("qno.list",'rb')
qnums=pickle.load(fp)
fp.close()
totndcg=dict.fromkeys(methods,0)
for qn in qnums[:35]:
	f=open('./queryResults/'+qn+'.txt')
	lines=f.readlines()
	f.close()
	#print 'for'+fil
	val={}
	filerank ={}
	for line in lines[1:]:
		linesplit=line.split()
		if linesplit[-1]!='-':
		    filerank[linesplit[0]]=int(linesplit[-1])
	for method in methods:
		fp=open('results/query_'+str(qn)+'_result_'+method+'_top_10.txt')
		methvals=fp.readlines()[1:]
		fp.close()
		val[method]=dcgcal(methvals,filerank,qn,method)/idcgcal(filerank)
	fp=open("ndcg/query_"+str(qn)+"_ndcg@10.txt",'w')
	for method in methods:
		fp.write(method+"	"+str(val[method])+"\n")
		if method=='cpes':
			fmain.write(str(val[method])+'\n')
		totndcg[method]=totndcg[method]+val[method]		
	fp.close()
fp=open("ndcg/ndcg@10.txt",'w')
for method in methods:
	fp.write(str(totndcg[method]/35)+"\n")	
fp.close()
print count	
