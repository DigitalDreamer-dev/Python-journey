x=int(input())
y=int(input())
'''
a=lambda x,y: x+y
b=lambda c: c*c
print(a(x,y))
print(b(x))'''
m=lambda a,b: a if a>b else b
print(m(x,y))




d=[1,2,3,4,5,6,7,8,9,10]
e=list(filter(lambda x:x%2==0, d))
print(e)
f=tuple(map(lambda x: x*x,d))
print(f)
x=[]
for i in d:
    x.append(i*i)
print(x)
