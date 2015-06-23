import pickle		
f=open('./trec_queries_flat_seg.txt','r')
lines=f.readlines()
l=0
path1="function.txt"#insert appropriate function word list here
f=open(path1,"r")
funcworden=f.read()
fp=open("qno.list",'rb')
qnums=pickle.load(fp)
fp.close()
funcworden=funcworden.split() 
for line in lines:
	f=open('./expansions/'+str(qnums[l])+'_flats.txt','w')
	a=line.split('|')
	for ex in a:
	    ex=ex.split()
	    if ex[0] in funcworden or ex[-1] in funcworden:
	    	continue
	    ex=' '.join(ex)
	    f.write(ex+'\n')
	l+=1
