lst=list(map(int,input().split()))
lst.sort()
c=0
for i in lst:
    if 1>i or i>=10**9:
        c=1
        exit(0)

maximum,minimum=0,0
for i in range(len(lst)):
    if i<=3:
        minimum+=lst[i]
    if i>=1:
        maximum+=lst[i]
print(minimum, maximum)
