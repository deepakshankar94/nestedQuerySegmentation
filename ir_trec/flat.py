import pickle
f=open('./trec_queries_flat_seg.txt','r')
lines=f.readlines()
l=0
fp=open("qno.list",'rb')
qnums=pickle.load(fp)
fp.close()
for line in lines:
	f=open('./expansions/'+str(qnums[l])+'_flat.txt','w')
	a=line.split('|')
	for ex in a:
	    ex=' '.join(ex.split())
	    f.write(ex+'\n')
	l+=1
