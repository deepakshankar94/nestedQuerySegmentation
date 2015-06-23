f=open('cpenscount.txt','w')
for i in range(1,501):
    fp=open('./expansions/'+str(i)+'_16.txt')
    a=fp.readlines()
    f.write(str(len(a))+'\n')
    fp.close()
f.close()   
