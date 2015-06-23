from __future__ import division
from math import log
import glob
import operator
import pickle
def apcal(fillist,filrank,valid1,filen,methn):
	num=1
	rel=0
	ap=0
	global fpmiss
	global count
	for url in fillist:
		url=url.split()[0]
		
		try:
			if filrank[url]==1:
				rel=rel+1
				ap=ap+(rel/num)
			num=num+1
		except KeyError:
			fpmiss.write(filen+'\n')
			fpmiss.write(methn+'\n')
			fpmiss.write(url+'\n')
			count=count+1
	#print 'yolo'
	return (ap/valid1)
		
	
count=0
methods=['kld','cpe','cpes']
totmap=dict.fromkeys(methods,0)
fp=open("qno.list",'rb')
qnums=pickle.load(fp)
fp.close()
fmain=open('mapall.txt','w')
fpmiss=open('missing_map.txt','w')
for qn in qnums[35:]:
	f=open('./queryResults/'+qn+'.txt')
	lines=f.readlines()
	f.close()
	val={}
	filerank ={}
	valid=0
	for line in lines[1:]:
		linesplit=line.split()
		if linesplit[-1]=='-':
		    #do nothing
		    xyzhdwh=0    
		elif int(linesplit[-1])==0:
			filerank[linesplit[0]]=0			    
		else:
			filerank[linesplit[0]]=1
			valid=valid+1
	for method in methods:
		fp=open('results/query_'+str(qn)+'_result_'+method+'_top_50.txt')
		methvals=fp.readlines()[1:]
		fp.close()
		val[method]=apcal(methvals,filerank,valid,qn,method)
	fp=open("map/query_"+str(qn)+"_ap@50.txt",'w')
	for method in methods:
		fp.write(method+"	"+str(val[method])+"\n")
		if method=='cpes':
			fmain.write(str(val[method])+'\n')	
		totmap[method]=totmap[method]+val[method]		
	fp.close()
fp=open("map/map@50.txt",'w')
for method in methods:
	fp.write(str(totmap[method]/40)+"\n")	
fp.close()
print count	
