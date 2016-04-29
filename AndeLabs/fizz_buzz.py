def fizz_buzz(number):
	"""
	Function fizz_buzz returns 
		-'Fizz' ==> if a number that is divisible by, 3
		-'Buzz' ==> if a number that is divisible by, 5
		-'FizzBuzz' ==> if a number that is divisible by both, 3 & 5
		-the argument it receives ==> when the number is not divisible by 3 or 5, 
	"""
	if (number % 3 == 0 and number % 5 != 0):
		return "Fizz"

 	elif (number % 5 == 0 and number % 3 != 0):
 		return "Buzz"

  	elif (number % 3 == 0 and number % 5 == 0):
  		return "FizzBuzz"
    
  	else:
  		return number

print fizz_buzz(2)
print fizz_buzz(33)
print fizz_buzz(20)
print fizz_buzz(30)