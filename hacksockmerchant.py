n=int(input())
lst=list(map(int,input().split()))
c=0

for i in lst:
    if i< 1 or i>100:
        c+=1

k,s,r=1,0,100

if 1<=n<=100 and c==0:
    for i in range(n):
        for j in range(n):
            if i>j or i<j:
                if lst[i]==lst[j]:
                    k+=1
                    lst[j]+=r
                    r+=100
        s+=(k//2)
        k=1
print(s)