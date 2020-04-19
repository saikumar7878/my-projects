num=int(input())
lst=list(map(int,input().split()))
lst1=[0,0,0,0,0]
if 5<=num<=(2*(10**5)):
    for k in lst:
        if k==1:
            lst1[0]+=1
        elif k==2:
            lst1[1]+=1
        elif k==3:
            lst1[2]+=1
        elif k==4:
            lst1[3]+=1
        elif k==5:
            lst1[4]+=1
    max,l=0,0
    for i in range(len(lst1)):
        if lst1[i]>max:
            max=lst1[i]
            l=i+1
    print(l)

    
