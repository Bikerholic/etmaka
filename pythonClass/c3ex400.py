inp1 = raw_input('Enter Score:')
try:
	score = float(inp1)
except:
	score = -1
if score > 0.00000000:
	if score < 0.60000000:
		print 'F'
	elif score <= 0.69900000:
		print 'D'
	elif score <= 0.79900000:
	    print 'C'
	elif score <= 0.89900000:
	    print 'B'
	elif score <= 1.00000000:
		print 'A'
	elif score > 1.000000000:
		print 'Number out of range'
else:
	print "This is not a number"

