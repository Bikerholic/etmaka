
def computegrade(s):
	if s > 1.0:
		print 'Number you entered is out of range'
		quit()
	if s > 0.00:
		if s < 0.600:
			g = 'F'
		elif s <= 0.699:
			g = 'D'
		elif s <= 0.799:
			g = 'C'
		elif s <= 0.899:
			g = 'B'
		elif s <= 1.00:
			g = 'A'
		print 'Finished with computegrade\n', 
	return g


inp1 = raw_input('Enter score (0.1 to 1.0): ')
try:
	score = float(inp1)
except:
	print 'Error, please enter a number.'
	quit()
	
# else:
# 	print "This is not a number"
grade = computegrade(score)
print 'Your final grade is a', grade


