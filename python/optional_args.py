# optional argument demo

def input_tuple(val, *input): # *input is type tuple
	if input:
		print(type(input))
		print(input)
	else:
		print(val)

def input_dic(val, **input): # **input is type dictionary
	if input:
		print(type(input))
		print(input)
	else:
		print(val)
    
def keyword(someval, type='', val = ''):
	if not type == '' and val == 2:
		print(type)
	else: 
		print('does not work')		
		
input_tuple('empty')
print('--------------------')
input_tuple('empty', 1,2,3,4)
print('--------------------')
input_dic('empty')
print('--------------------')
input_dic('empty', input='1')
print('--------------------')
keyword(1)
keyword(1,val=1,type=2)
keyword(1,type=1, val=2)
