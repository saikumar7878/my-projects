b,n,m=map(int,input().split())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))

sum,a=0,0

for i in range(n):
    for j in range(m):
        sum=lst1[i]+lst2[j]
        if sum<b:
            if sum>a:
                a=sum
if a>0:
    print(a)
else:
    print('-1')
    
