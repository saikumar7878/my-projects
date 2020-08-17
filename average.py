lst=list(map(int, input().split()))
def aver(lst):
    sum,c=0,0
    for i in lst:
        sum=sum+i
        c+=1
    return float(sum/c)
f=aver(lst)
print("{:.2f}".format(f))

