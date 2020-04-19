t=int(input())
lst,lst2=[],[]
h=1
for i in range(t):
    c=int(input())
    lst.append(c)

for l in lst:
    h=1
    for i in range(l):
        if i%2!=0:
            h*=2
        elif i==0:
            h=1
        else:
            h+=1
    lst2.append(h)

for l in lst2:
    print(l)