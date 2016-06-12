#.................................................#
#                                                 #
#  This program takes your weekly work hours and  #
#  calculate regular pay along with overtime pay  #
#  K.Mau 06-11-16 Brooklyn, NY                    #
#                                                 #
#.................................................#

#  Ask user to enter their work hours
#  Assign the answer from the user to a variable 'inp1'
inp1 = raw_input('Enter total week worked hours: ')
#  Check(1) if entered value is a number, an integer
try:
	#  Assign new name 'totalHours' to variable 'inp1'
	#  Convert user entered answer into floating point
	#  If can't convert, then the value must be string
	totalHours = float(inp1)
#  Checked(1) and its not a number or an integer
#  Execute the following
except:
	#  Set this non number, non interger
	#  Set this string value to -1
	totalHours = -1
#  If the total worked hours is greater than zero
if totalHours > 0.0:
	#  And if the total worked hours is greater to 40
	if totalHours > 40.0:
		#  Assign a new variable 'totalOtHours'
		#  Set the formula equal to total hours minus 40
		totalOTHours = totalHours - 40.0
	#  If total hours is less than or equal to 40
	if totalHours <= 40.0:
		#  Therefor the total overtime hours is set zero
			totalOTHours = 0.0
#  Checked(1) and its a string
#  Therefor execute the following
else:
	#  Print the follow statement
	print 'I am sorry, that is not a number.'

#  Ask user to enter their hourly rate
#  Assign the answer from the user to a variable 'inp2'
inp2 = raw_input('Enter your hourly rate: ')
#  Check(2) if entered value is a number, an integer
try:
	#  Assign new name 'hourlyRate' to variable 'inp2'
	#  Convert user entered answer into floating point
	#  If can't convert, then the value must be string
	hourlyRate = float(inp2)
#  Checked(2) and its not a number or an integer
#  Execute the following
except:
	#  Set this non number, non interger
	#  Set this string value to -1
	hourlyRate = -1
#  If the hourly rate is greater than zero
if hourlyRate > 0.0:
	#  If the total worked hours is less than or equal to 40
	if totalHours <= 40.0:
		#  Assigne a new variable 'totalWage'
		#  Calculate 'totalWage' by multying total hours by hourly rate
		totalWage = totalHours * hourlyRate
		#  Print string concatenated wtih the variable 'tatalWage'
		print "Your total pay is $", totalWage
	#  If total worked hours is greater than 40
	if totalHours > 40.0:
		#  Then there must be overtime hours
		#  Assign a new variable to 'totalOTWages'
		#  Set the formula for overtime wage by
		#  multiplying total overtime hours 
		#  by one and half time hourly rate
		totalOTWages = totalOTHours * (hourlyRate * 1.5)
		#  Calculate totalWage by multiply 40 by hourly rate
		totalWage = 40.0 * hourlyRate
		#  Print string concatenated with the variable 'totalOTHours'
		print 'Total number of overtime hours is',totalOTHours
		#  Print string concatenated with with a variable totalOTWages
		#  Request a new line, string concatenated with a variable 'totalWage' 
		print "Total overtime pay is $",totalOTWages,"\nTotal regular wage is $",totalWage
		#  Assign a new variable 'totalPaywithOT'
		#  Calculate pay with OT, set formula to
		#  'totalPaywithOT' equal standard week pay plus OT pay
		totalPaywithOT = (40.0 * hourlyRate) + totalOTWages
		#  Print string concatenated with a variable 'totalPaywithOT'
		print "Total pay plus overtime is $",totalPaywithOT
#  Checked(2) can't be coverted to a number and must a string
#  Therefor execute the following
else:
	#  Print the follow statement
	print 'I am sorry, that is also not a number.'



