from __future__ import division
import pickle
f=open('cpenscount.txt','w')
fp=open("qno.list",'rb')
qnums=pickle.load(fp)
fp.close()
fp=open('fildict.txt','rb')
querystr=pickle.load(fp)
fp.close()
qlen=[3,4,5,6,7,8]
exptot=dict.fromkeys(qlen,0)
expnum=dict.fromkeys(qlen,0)
for i in qnums:
    fp=open('./expansions/'+str(i)+'_16.txt')
    ql=len(querystr[i])
    a=fp.readlines()
    print ql
    f.write(str(len(a))+'\n')
    exptot[ql]+=len(a)
    expnum[ql]+=1
    fp.close()
f.close()   
for i in exptot.keys():
    if expnum[i]!=0:
        print i
        print exptot[i]/expnum[i]  
