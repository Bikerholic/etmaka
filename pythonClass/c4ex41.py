def computepay(h,r):
	print 'In computepay', h, r
	if h <= 40:
		p = r * h
	else:
		p = r * 40 + ( r * 1.5 * ( h - 40 ))
	print 'Finished with computepay', p
	return p

try:
	inp1 = raw_input('Enter Hours: ')
	hours = float(inp1)
	inp2 = raw_input('Enter Rates: ')
	rates = float(inp2)
except:
	print "Error, please enter numberic input"
	quit()
print 'In the main code', hours, rates
pay = computepay(hours,rates)
print 'We are back', pay
