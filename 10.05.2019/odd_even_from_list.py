x=[1,2,3,4,5,9,10]
even=0
odd=0
for i in range(0,len(x),1):
    if x[i]%2==0:
        even=even+1
    else:
        odd=odd+1

print "No of even is ",even
print "No of odd is ",odd
