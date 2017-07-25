import sys
import time
import win32api
import os

def clear():  # clear terminal
	os.system('cls')
	
def getInput(): # get user input
	x = int(input('time: '))
	return x 

def timer(getInput):  # timer function
	x = getInput
	
	for i in range(x, 0, -1):
		time.sleep(1)
		sys.stdout.write("\r%ds left" % i)
		sys.stdout.flush()
	
	win32api.MessageBox(0, 'Done', 'timer')
	clear()	
  
  
try:
	timer(getInput())
except Exception as e:
	win32api.MessageBox(0, str(e.__class__.__name__) + ' : ' + str(e), 'Error!')
