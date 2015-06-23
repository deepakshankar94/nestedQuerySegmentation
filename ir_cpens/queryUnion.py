import pickle
f=open("QueryTestSetWithQueryIndex.txt")
lines=f.readlines();
queries=[]
for i in lines:
	queries+=i.split()[1:]
queries=list(set(queries))
fp=open('queryset.list','wb')
pickle.dump(queries,fp)
print len(queries)
