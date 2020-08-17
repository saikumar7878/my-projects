import math
num=int(input())
lst=[]
if 1<=num<=100:
    for i in range(num):
        a,b=map(int,input().split())
        count=0
        if 1<=a<=b<=10**9:
            for j in range(a,b+1):
                root=math.sqrt(j)
                if int(root+0.5)**2==j:
                    count+=1
        else:
            exit(0)
        lst.append(count)
    for l in lst:
        print(l)