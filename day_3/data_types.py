def data_type(x):
	'''
	Takes in an argument,x:
		- For an integer, return x**2
		- For a float, return x/2
		- For a string, return "hello" + x
		- For a boolean, return "boolean"
		- For a long, squareroot(x)
	'''

	if type(x) == int:
		return x ** 2
	elif type(x) == float:
		return x / 2
	elif type(x) == str:
		return "Hello {}".format(x)
	elif type(x) == bool:
		return "boolean"
	elif type(x) == long:
		return "long"


print data_type(2)
print data_type(2.4)
print data_type("Joy")
print data_type(True)
print data_type(2**50)