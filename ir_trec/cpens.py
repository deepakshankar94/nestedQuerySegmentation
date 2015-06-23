import glob
from nltk.tree import Tree
import pickle
def expand(tr,fp,firw):
	for node in list(tr.subtrees())[1:]:
		if len(node)!=0:
			printt(node,fp,firw)
				
def printt(nodes,fp,firw):
	pstr=''
	global funcworden
	for node in nodes.subtrees():
		if len(node)==0:
			pstr=pstr+node.__str__()[1:-1]
	pstr=pstr.split()
	if (pstr[0] in funcworden and pstr[0]!=firw) or pstr[-1] in funcworden:
		return	
	pstr=' '.join(pstr)
	fp.write(pstr)
	fp.write('\n')
def printroot(root,fp):
	pstr=''
	for node in root.subtrees():
		if len(node)==0:
			pstr=pstr+node.__str__()[1:-1]
	pstr=pstr.split()
	pstr=' '.join(pstr)
	fp.write(pstr)
	fp.write('\n')
	return pstr.split()
		
files=glob.glob("./Nested/*")
files=sorted(files)
path1="function.txt"#insert appropriate function word list here
f=open(path1,"r")
funcworden=f.read()
funcworden=funcworden.split()  
print len(files)
fp=open("qno.list",'rb')
qnums=pickle.load(fp)
fp.close()
print files
m=15
l=0
f=open('trec_scheme_016_S_OP_J_CD.txt','r')
print f
lines=f.readlines()
for line in lines:
	t=Tree(line)
	f=open('./expansions/'+str(qnums[l])+'_'+str(m)+'.txt','w')
	qsplit=printroot(t,f)
	expand(t,f,qsplit[0])
	l+=1

