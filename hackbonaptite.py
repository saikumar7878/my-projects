n,k=map(int,input().split())
lst=list(map(int, input().split()))
b=int(input())
c,s,tot=0,0,0

for i in lst:
    if 0<=i<=10**4:
        c=0
    else:
        c=1
        break
for i in lst:
    s=s+i

if 2<=n<=10**5 and 0<=k<=n and c==0 and 0<=b<=s:
    for i in range(len(lst)):
        if i==k:
            continue
        else:
            tot+=lst[i]
    tot/=2
    if tot==b:
        print("Bon Appetit")
    else:
        print(int(b-tot))