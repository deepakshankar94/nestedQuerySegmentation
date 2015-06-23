import glob
files=[]
for file in glob.glob("./queryResults/*"):
	f=open(file,'r')
	files+=f.readlines()
	f.close()
files=list(set(files))
f=open('collection.txt','w')
files=[(a.split("\\"))[2] for a in files]
f.writelines(files)
