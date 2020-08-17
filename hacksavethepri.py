t=int(input())
lst=[]
if 1<=t<=100:
    for i in range(t):
        n,m,s=map(int,input().split())
        if (s+m-1)%n==0:
            lst.append(n)
        else:
            lst.append((s+m-1)%n)
    for l in lst:
        print(l)