class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def are(self):
        return self.x*self.y
class Circle:
    def __init__(self1,r):
        self1.r=r

    def are2(self1):
        return self1.r*self1.r*3.14

x,y=map(int,input().split())
r1=Rectangle(x,y)
r=int(input())
c1=Circle(r)
arr1=r1.are()
arr2=c1.are2()
print(arr1,arr2)