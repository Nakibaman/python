for i in range(1,8,1):
    for j in range(1,8,1):
        if i==1 or i==7 or j==1 or j==7 or i==j or i+j-1==7:
            print "*",
        else:
            print " ",
    print ""
