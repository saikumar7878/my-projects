import random
lst=list(map(int,input().split()))
lst2=[]
n=len(lst)
for i in range(len(lst)):
    c=1
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j] and lst[i]!='visited':
            c=c+1
            lst[j]='visited'
    if lst[i]!='visited' and  c>len(lst)//3:
        lst2.append(lst[i])
if len(lst2)!=0:
    print(random.choice(lst2))