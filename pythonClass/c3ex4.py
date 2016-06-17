inp1 = raw_input("Enter Score: ")
try:
    score = float(inp1)
except:
    score = -1
if score > 1.0:
    print "This number is out of range 0 to 1"
   # if score > 0.0 and < 1.1:
        if score >= 0.9:
            print "A"
        if score >= 0.8:
            print "B"
        if score >=0.7:
            print "C"
        if score >=0.6:
            print "D"
        if score >=0.1:
            print "F"
else:
    print "This is not a number"