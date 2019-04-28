print "Enter a midterm mark"
mark=int(raw_input())
if mark<0 or mark>30:
    print "Invalid mark"
else:
    if mark<=3:
        print "Failed"
    else:
        print "Passed"

