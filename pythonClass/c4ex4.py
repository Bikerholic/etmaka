def computepay(hr,ra):
	print 'In computepay H=',hr,'R=',ra
	if hr <= 40:
		py = ra * hr
	else:
		py = ra * 40.00 + (ra * 1.50 * (hr - 40))
		ot = ra * 1.5 *(hr - 40.0)
	print 'Your total OT pay is $',ot
	print "Finished with computepay",py
	return py

try:
	inp1 = raw_input('Enter Hours: ')
	hours = float(inp1)
	inp2 = raw_input('Enter Rate: ')
	rate = float(inp2)
except:
	print "Error please enter numeric input"
	quit()
# if hours <= 40:
# 	pay = rate * hours
# else:
# 	pay = rate * 40.00 + (rate * 1.50 * (hours - 40))
pay = computepay(hours,rate)
print pay