print "Enter Banglar mark"
bng=int(raw_input());
print "Enter Mather mark"
mth=int(raw_input());
print "Enter Sciencer mark"
snc=int(raw_input());

if (bng>=30 and mth>=30 and snc>=30) or (bng>=30 and mth>=40 or snc>=40):
    print "Welcome"
else:
    print "Not welcome"
