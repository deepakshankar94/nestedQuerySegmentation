		
f=open('./flat.txt','r')
lines=f.readlines()
l=1
path1="function.txt"#insert appropriate function word list here
f=open(path1,"r")
funcworden=f.read()
funcworden=funcworden.split() 
for line in lines:
	f=open('./expansions/'+str(l)+'_flat.txt','w')
	a=line.split('|')
	for ex in a:
	    ex=ex.split()
	    if ex[0] in funcworden or ex[-1] in funcworden:
	    	continue
	    print ex
	    ex=' '.join(ex)
	    f.write(ex+'\n')
	l+=1
