n=int(input())
str=input()
c,s=0,0

"""for i in str:
    if i!="U" or i!="D":
        c+=1
    print(c,i)
"""
if 2<=n<=10**6 and c==0:
    for i in range(n):
        if str[i]=='U':
            continue
        else:
            if str[i+1]=='U':
                s+=1
    print(s)