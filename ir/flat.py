		
f=open('./flat.txt','r')
lines=f.readlines()
l=1
for line in lines:
	f=open('./expansions/'+str(l)+'_flat.txt','w')
	a=line.split('|')
	for ex in a:
	    ex=' '.join(ex.split())
	    f.write(ex+'\n')
	l+=1
