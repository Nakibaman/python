import numpy as n
a=n.array([[1,2,3],[4,5,6]])
b=n.array([[1,1,1],[2,2,2]])
for i in range(0,2,1):
    for j in range(0,3,1):
        a[i,j]=a[i,j]+b[i,j]
    print 


for i in range(0,2,1):
    for j in range(0,3,1):
        print a[i,j],
    print
