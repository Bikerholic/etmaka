
try:
	inp = raw_input('Enter hours ')
	hours = float(inp)
	inp = raw_input('Enter rates ')
	rates = float(inp)
except:
	inp = -1
	print 'error'
	quit()

# print rate, hours
# if hours > 0:
# 	if hours <= 40.00:
# 	    pay = rates * hours
# 	    return type(pay)
# 	if hours > 40.00:
# 	pay = rates * 40.00 + (rates * 1.50 (hours - 40))
# else:
# 	print pay
