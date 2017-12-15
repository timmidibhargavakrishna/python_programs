string=input()
list1=[]
list2=[]
distnary={}
for i in range(len(string)):
    if(string[i]=='F'):
        list1.append(string[i])
    else:
        list2.append(string[i])
print('F_COUNT=',len(list1),'M_COUNT=',len(list2))
distnary={'Femals':list1,'Males':list2}
print(''.join(distnary['Femals']),end='')
print(''.join(distnary['Males']))