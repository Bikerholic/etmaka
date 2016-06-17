#This program takes Celsius and calculate it
#into the corresponding value in Fahrenheit
#K.Mau 06-11-16 Brooklyn, NY
#
#Assign the variable 'inp1' for input #1
#Request user to input temperature in Celsius
inp1 = raw_input('Enter Celsius: ')
#Convert the type of the variable 'inpu1' 
#from a interger into floating point unit.
#Assign the variable 'inp1' into 'celisiusValue' 
celisiusValue = float(inp1)
#Output of entered value with concatenated strings
print 'For',celisiusValue,'C degree in Celisius'
#Calculated fahrenheit value, doing the math bit.
fahrenheitValue = celisiusValue * 9.0 / 5.0 + 32.0
#Output of calculated with concatenated strings. 
print 'It is',fahrenheitValue,'F degree in Fahrenheit'

