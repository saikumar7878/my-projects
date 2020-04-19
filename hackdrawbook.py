n=int(input())
k=int(input())
c,s=0,0

if 1<=n<=10**5 and 1<=k<=n:
    for i in range(1,n,2):
        if i<k:
            c+=1
    if n%2==0:
        n=n-1
        s=1

    for i in range(n,1,-2):
        if i>=k:
            s+=1
        else:
            s=s-1
            break

    if s>c:
        print(c)
    else:
        print(s)