def factorial(number):
	"""
	Function factorial(number), takes the number parameter been passed and return the factorial of it.
		e.g. if number is 4, it should return (4 * 3 * 2 * 1) which is 24
	"""
  if number == 0:
    return 1
  else:
    return number * factorial(number-1)

print factorial(1) 
print factorial(4) 
print factorial(5) 