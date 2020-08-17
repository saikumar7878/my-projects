n,k=map(int,input().split())
lst=list(map(int,input().split()))
l=0
for i in lst:
    if i==0 or i==1:
        continue
    else:
        l=l+1
        break 
if 2<=n<=25 and 1<=k<=n and n%k==0 and l==0:
    ene,c=100,0
    for i in range(0,n,k):
        if lst[i]==1:
            c=c+3
        else:
            c=c+1
    print(ene-c)
    