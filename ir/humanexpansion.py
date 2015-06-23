import glob
from nltk.tree import Tree
def expand(tr,fp):
	for node in tr.subtrees():
		if len(node)!=0:
			printt(node,fp)
				
def printt(nodes,fp):
	for node in nodes.subtrees():
		if len(node)==0:
			fp.write(node.__str__()[1:-1])
	fp.write('\n')
		
#files=glob.glob("./Nested/*")
file='./Nested/SGCL12_Nested_Anno3.txt'
print file
m=16
f=open(file,'r')
lines=f.readlines()
l=1
for line in lines:
	t=Tree(line)
	f=open('./expansions/'+str(l)+'_h3.txt','w')
	expand(t,f)
	l+=1

