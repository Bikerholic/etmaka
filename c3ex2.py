#:Colon symbol - Expicit expect next line indented 
#Request user to enter a number
#Assign this number to a new variable 'inp1'
inp1 = raw_input('Enter total work hours for the week:')
#inp2 = raw_input('Enter a rate:')
#Test to see if the value entered is a number
try:
	#Assign the new variable to a new name 'ival'
	#Check if entered value is a number, an integer 
	ival = float(inp1)
#If entered value is not a number, an integer
except:
	#Assign the value of -1 to the variable 'ival'
	ival = -1
#Check if the integer value is greater than 0
if ival > 0:
	#Check if the integer value is lesser than 10
	if ival < 40:
		#If it is less than 10, print statement
		print 'Total regular pay hours:',ival
	if ival == 40:
		print 'Total regular pay hours:',ival
	#Check if the integer value is greater than 10
	if ival > 40:
		ivalTotal = ival % 40
		#If it is greater than 10, print statment
		print 'Total regular pay hours:40 \nTotal Overtime pay hours:',ivalTotal
#If the variable 'inp1' is a string and not a number
#Print statement
else:
	print 'This thing here is not a number'

inp2 = raw_input('Enter your hourly rate :')
try:
	ival2 = float(inp2)
except:
	ival2 = -1
if ival2 > 0 and ival <= 40:
	ival2Total = ival * ival2
	print 'Total pay without overtime $',ival2Total
if ival2 > 0 and ival > 40:
	totalOT = ivalTatal * 1.5
	ival3Total = ival * ival2 + totalOT * 1.50
	print 'Total overtime pay $'
	print 'Total pay with ovetime $',ival3Total
else:
	print 'This thing here is not a number'

