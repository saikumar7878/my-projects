lst=list(map(int,input().split()))
lst2=[]
for i in range(len(lst)):
    c=1
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j] and lst[i]!='visited':
            c=c+1
            lst[j]='visited'
    if lst[i]!='visited':
        lst2.append(c)
for i in range(len(lst2)):
    for j in range(i+1,len(lst2)):
        if lst2[i]==lst2[j]:
            print('false')
            exit(0)
print('true')


