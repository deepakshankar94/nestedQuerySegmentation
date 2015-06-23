from itertools import chain, combinations
import nltk
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(2,len(s)+1))

def subsets(s):
    return map(list, powerset(s))
def goodstopword(subquery,pos,qsb):
	left=0
	right=0
	for i in range(pos+1,len(subquery)):
		if (subquery[i-1][1] == subquery[i][1]-1) and ( subquery[i][2]==1 or  subquery[i][1]==len(qsb)-1) :
			right=1
			break
		elif subquery[i-1][1] != subquery[i][1]-1:
			break
	for i in range(pos-1,-1,-1):
		if (subquery[i+1][1] == subquery[i][1]+1) and (subquery[i][2]==1 or subquery[i][1]==0):
			left=1
			break
		elif subquery[i+1][1] != subquery[i][1]+1:
			break
	if left==1 and right ==1:
		return True
	else:
		return False
		
def cpes(allqsub,qsb):
	flag=0
	correct=[]
	for subquery in allqsub:
		flag=0
		
		for i in range(len(subquery)):
			if subquery[i][2]==1:
				continue
			else:
				if subquery[i][1]==0 and subquery[i+1][1]!=1 or subquery[i][1]==len(qsb)-1 and subquery[i-1][1]!=len(qsb)-2:
					flag=1
					break
				elif subquery[i][1]==0 and subquery[i+1][1]==1 or subquery[i][1]==len(qsb)-1 and subquery[i-1][1]==len(qsb)-2:
					continue
				elif goodstopword(subquery,i,qsb):
					continue
				else:
					flag=1
					break
		if flag==0:
			correct.append(subquery)
	return correct
		

def cpe(allqsub,qsb):
	flag=0
	correct=[]
	for subquery in allqsub:
		flag=0
		
		for i in range(len(subquery)):
			if subquery[i][2]==1:
				continue
			else:
				flag=1
		if flag==0:
			correct.append(subquery)
	return correct
	
	
fp=open("query_clean_list.txt",'r')
queries=fp.readlines()
fp.close()
for query in queries:
	query=query.split()
	qno=query[0]
	qsb=query[1:]
	qsb=[wor.lower() for wor in qsb ]
	path1="stops.txt"#insert appropriate stop word list here
	f=open(path1,"r")
	stopworden=f.read()
	stopworden=stopworden.split()  
	qsp=[]
	i=0
	for word in qsb:
		if word in stopworden:
			qsp.append((word,i,0))
			i+=1
		else:
			qsp.append((word,i,1))
			i+=1
	allqsub=subsets(qsp)
	ccpe=cpe(allqsub,qsb)
	ccpes=cpes(allqsub,qsb)
	focpe=open('./cpe/'+qno+'_cpe.txt','w')
	focpes=open('./cpes/'+qno+'_cpes.txt','w')
	for item in ccpe:
		for tuplew in item:
			focpe.write("%s " % tuplew[0])
		focpe.write('\n')
	for item in ccpes:
		for tuplew in item:
			focpes.write("%s " % tuplew[0])
		focpes.write('\n')					
