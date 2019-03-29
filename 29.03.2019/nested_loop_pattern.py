for i in range(1,6,1):
    for j in range(1,6,1):
        if i==1 or i==5 or j==1 or j==5 or i==3 or j==3:
            print "*",
        else:
            print " ",
    print ""
