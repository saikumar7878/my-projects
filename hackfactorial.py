num=int(input())
if 1<=num<=100:
    fact=1
    for i in range(1,(num+1)):
        fact*=i
    print(fact)