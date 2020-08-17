t=int(input())
lst=[]
for i in range(t):
    x=int(input())
    lst.append(x)
lst3=[]
for i in range(t):
    k=lst[i]
    c,lst2=0,[]
    while(k):
        r=k%10
        k=k//10
        lst2.append(r)
    for j in lst2:
        try:
            if lst[i]%j==0:
                c=c+1
        except ZeroDivisionError:
            continue
    lst3.append(c)
for i in lst3:
    print(i)