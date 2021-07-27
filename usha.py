a=[1, 2, 3, 4, ]
i=0
a=[]
while i<=8:
    j=str(a[i])+str(a[i+1])
    a.append(j)
    i=i+1
print(a)

a=[1, 2, 3, 4, 5, 6]
i=1
p=a[0]
b=[]
while i<len(a):
    d=a[i]
    j=b-d
    b.append(j)
    p=d
    i=i+1
    print(b)