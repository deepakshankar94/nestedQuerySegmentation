import glob
from nltk.tree import Tree
def expand(tr,fp):
	for node in tr.subtrees():
		if len(node)!=0:
			printt(node,fp)
				
def printt(nodes,fp):
	pstr=''
	global funcworden
	print nodes
	for node in nodes.subtrees():
		if len(node)==0:
			pstr=pstr+node.__str__()[1:-1]
	pstr=pstr.split()
	print pstr
	if pstr[0] in funcworden or pstr[-1] in funcworden:
		return	
	pstr=' '.join(pstr)
	fp.write(pstr)
	fp.write('\n')
		
files=glob.glob("./Nested/*")
files=sorted(files)
path1="function.txt"#insert appropriate function word list here
f=open(path1,"r")
funcworden=f.read()
funcworden=funcworden.split()  
print len(files)
m=1
for file in files:
	f=open(file,'r')
	print file
	lines=f.readlines()
	l=1
	for line in lines:
		t=Tree(line)
		f=open('./expansions/'+str(l)+'_'+str(m)+'.txt','w')
		expand(t,f)
		l+=1
	m+=1
