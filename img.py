num=input()
l=len(num)
sum=0
for i in range(l):
    if i%2!=0 or i==0:
        sum+=int(float(num[i]))
    else:
        sum*=int(float(num[i]))
print(sum)

