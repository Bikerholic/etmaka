#  
#  My first function
#  def to define a function
#  hello() is his name
#  
#  def - define the function
#  Stored within the () are the parameters
#  Of which this had none
#
def hello():
	print 'Hello'
	print 'Fun'
def print_lyric():
	print"I'm a lumberjack, and I'm okay."
	print 'I sleep all night and i work all day.'
hello()
print_lyric()
print "Zip"

hello()

##
##  When executed within shell
##
##  enter greet('es')
##   returned 'Hola'
##  enter greet('fr')
##   returned 'Bonjour'
##  enter greet('en')
##    returned 'Hello'
##
##  This is called defining parameters.
##  lang is the name, 3 parameters.
def greet(lang):
    if lang == 'en':
        return 'Sup, man.'
    if lang == 'es':   # Param 01
        return 'Hola'   #  Then
    elif lang == 'fr': # Param 02
        return 'Bonjour'#  Then
    else:			   # Param 03
        return 'Hello'  #  Then

##  print greet('es'),'Sally'
##    Return Hola Sally
##  print greet('fr'),'Michael'
##    Return Bonjour Michael
##  When imputs number is 5, 
##  
inp1 = raw_input('Enter number: ')

##  Try ensuring we're dealing 
##  numbers here.
##
try:
	num = int(inp1)
except:
	num = -1
# 
if num == 5:
	print 'Hello'
print 'Yo'
print_lyric()
num = num + 2
print num

def addtwo(a,b):
    added = a + b
    return added
x = addtwo(3,5)
print (' ')
print 'def addtwo function,\nadded = a + b,\nreturn added'
print (' ')
print 'x = addtwo(3,5)\nprint x'
print (' ')
print x


