#:Colon symbol - Expicit expect next line indented 
#Request user to enter a number
#Assign this number to a new variable 'inp1'
inp1 = raw_input('Enter a number:')
inp2 = raw_input('Enter a rate:')
#Test to see if the value entered is a number
try:
	#Assign the new variable to a new name 'ival'
	#Check if entered value is a number, an integer 
	ival = int(inp1)
#If entered value is not a number, an integer
except:
	#Assign the value of -1 to the variable 'ival'
	ival = -1
#Check if the integer value is greater than 0
if ival > 0:
	#Check if the integer value is lesser than 10
	if ival < 40:
		#If it is less than 10, print statement
		print 'Nice Work it is smaller than 40'
	if ival == 40:
		print 'Nice Work it is exact 40'
	#Check if the integer value is greater than 10
	if ival > 40:
		#If it is greater than 10, print statment
		print 'This number is greater than 40'
#If the variable 'inp1' is a string and not a number
#Print statement
else:
	print 'This thing here is not a number'


