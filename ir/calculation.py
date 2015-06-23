import pickle
import glob
f=open('queryset.list')
qlist=pickle.load(f)
f.close()
cf=dict.fromkeys(qlist,0)
collen=0
fp=open('collection.txt','r')
colfiles=fp.readlines()
fp.close()
for file in colfiles:
    f=open('./Document Collection/'+file[:-2])
    words=f.read().split()
    words=[x.lower() for x in words]
    f.close()
    print 'reading file '+file
    df=dict.fromkeys(qlist,0)
    poslist=dict.fromkeys(qlist)
    pos=0
    for word in words:
    	if word in qlist:
    		cf[word]+=1
    		df[word]+=1
    		if poslist[word]==None:
    			poslist[word]=[pos]
    		else:
    			poslist[word]+=[pos]
    	pos+=1
    	collen+=1
    f=open('position list/df_'+file[:-2],'wb')
    pickle.dump(df,f)
    f.close()
    f=open('position list/poslist_'+file[:-2],'wb')
    pickle.dump(poslist,f)
    f.close()
    f=open('position list/len_'+file[:-2],'wb')
    pickle.dump(pos,f)
    f.close()
f=open('position list/cf.txt','wb')
pickle.dump(cf,f)
f.close()
f=open('position list/collen.txt','wb')
pickle.dump(collen,f)
f.close()
    
    
