# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from openpyxl import Workbook
import re

class Check:
	def __init__(self):
		self.stat = ''
	
	def isEnglish(self, s): # check if input is non-english
		if s != None:
			try:
				str(s).encode('ascii')
			except UnicodeEncodeError:
				return False
			else:
				return True
		return True	
	
	def isDigit(self, s): # check if input is only made with number 
		return s.isdigit()
		
	def isNumber(self, s):  # check if input is a number
		try:
			float(s) # for int, long and float
		except ValueError:
			try:
				complex(s) # for complex
			except ValueError:
				return False
		return True
		
	def checkFormat(self, cell, type): # check string format using general expression
		if 'Cell' in str(cell):
			print('this is cell')
			s = cell.value
		else:
			s = cell
		if type.lower() == 'else':
			r = re.compile('[a-zA-Z0-9_]')
			if r.match(s):
				return True
			else:
				return False
		elif type.lower() == 'time':
			r = re.compile("[0-9]{2}:[0-9]{2}")
			if re.match(r,s):
				return True
			else:
				r = re.compile(".{1}: [0-9]{2}:[0-9]{2}")
				if re.match(r,s):
					return True
				else:
					r = re.compile(".{1}-.{1}: [0-9]{2}:[0-9]{2}")
					if re.match(r,s):
						s = s.split(':')[0]
						return True
		return False
    
	def tryIndex(self, list, index): # check if list has certain index
		try:
			data = list[index]
		except IndexError:
			data = None
		return data
		
	def getSubStr(start,end,s): # return string between start and end string 
		r = re.findall('%s(.*)%s' % (start, end), s)
		return r
			
