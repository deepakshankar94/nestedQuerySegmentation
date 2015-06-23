import pickle
f=open("query_clean_list.txt")
lines=f.readlines();
queries=[]
for i in lines:
	queries+=i.split()[1:]
queries=list(set(queries))
print queries
fp=open('queryset.list','wb')
pickle.dump(queries,fp)
fp.close()
print len(queries)
