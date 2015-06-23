from __future__ import division
f=open('cpencount.txt','w')
fp=open('QueryTestSetWithQueryIndex.txt','r')
queries=fp.readlines()
fp.close()
qlen=[3,4,5,6,7,8]
exptot=dict.fromkeys(qlen,0)
expnum=dict.fromkeys(qlen,0)
for i in range(1,501):
    fp=open('./expansions/'+str(i)+'_16.txt')
    ql=len(queries[i-1].split())-1
    a=fp.readlines()
    f.write(str(len(a))+'\n')
    exptot[ql]+=len(a)
    expnum[ql]+=1
    fp.close()
f.close()
for i in exptot.keys():
    if expnum[i]!=0:
        print i
        print exptot[i]/expnum[i]  

