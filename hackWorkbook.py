n,k=map(int,input().split())
lst=list(map(int,input().split()))
c,p=0,0

for i in range(1,n+1):
    if lst[i-1]%k==0:
        p=p+lst[i-1]//k
    else:
        p=p+lst[i-1]//k+1
print(p)