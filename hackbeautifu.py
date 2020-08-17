s,t,k=map(int,input().split())
c=0
for i in range(s,(t+1),1):
    r,n=0,i
    while(i>0):
        re=i%10
        r=(r*10)+re
        i//=10
    if (n-r)%k==0:
        c+=1
print(c)