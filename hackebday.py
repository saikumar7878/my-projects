num=int(input())
lst=list(map(int,input().split()))
d,m=map(int, input().split())
c,sum,l=0,0,0
for k in lst:
    if 1<=k<=5:
        continue
    else:
        l=l+1
if 1<=num<=100 and 1<=d<=31 and 1<=m<=12 and l==0:
    if m>1:
        for i in range(len(lst)):
            for j in range(m):
                if i+j<len(lst):
                    sum+=lst[i+j]
            if sum==d:
                c=c+1
            sum=0
    else:
        for i in range(len(lst)):
            for j in range(m):
                    sum+=lst[i+j]
            if sum==d:
                c=c+1
            sum=0
    print(c)
