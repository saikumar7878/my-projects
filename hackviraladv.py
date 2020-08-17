num=int(input())
like,share,cumulative=0,5,0
k=share
if 1<=num<=50:
    for i in range(num):
        like=k//2
        cumulative+=like
        k=like*3
    print(cumulative)