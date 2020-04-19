num,k=map(int,input().split())
lst=list(map(int,input().split()))
c,l,sum=0,0,0
for i in lst:
    if i>100 or i<1:
        l=l+1
if 2<=num<=100 and 1<=k<=100 and l==0: 
    for i in range(num):
        sum=lst[i]
        for j in range(num):
            if i<j:
                sum=sum+lst[j]
                if sum%k==0:
                    c+=1
                sum=lst[i]
print(c)
