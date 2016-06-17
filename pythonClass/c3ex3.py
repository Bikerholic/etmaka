inp1 = raw_input('Enter total week worked hours: ')
try:
	totalHours = float(inp1)
except:
	totalHours = -1

if totalHours > 0.0:
	if totalHours > 40.0:
		totalOTHours = totalHours - 40.0
	if totalHours <= 40.0:
		totalOTHours = 0.0
else:
	print 'I am sorry, that is not a number.'

inp2 = raw_input('Enter your hourly rate: ')
try:
	hourlyRate = float(inp2)
except:
	hourlyRate = -1
if hourlyRate > 0.0:
	if totalHours <= 40.0:
		totalWage = totalHours * hourlyRate
		print "Your total pay is $", totalWage
	if totalHours > 40.0:
		totalOTWages = totalOTHours * (hourlyRate * 1.5)
		totalWage = 40.0 * hourlyRate
		print 'Total number of overtime hours is',totalOTHours
		print "Total overtime pay is $",totalOTWages,"\nTotal regular wage is $",totalWage
		totalPaywithOT = (40.0 * hourlyRate) + totalOTWages
		print "Total pay plus overtime is $",totalPaywithOT
else:
	print 'I am sorry, that is also not a number.'

