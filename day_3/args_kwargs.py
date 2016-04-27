def hello(name,age):
	'''
	'''
	return "I am {}, and I am {}".format(name,age)

people = [
			("Jane", 23),
			("Joe", 25),
			("Ryan", 60),
			("Betty", 25)
			]

for item in people:
	print hello(*item)

'''
for name,age in people:
	print hello(name,age)
'''

def super_sum(*args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g. super_sum(10, 20) =30
		super_sum(10,20,40) =70
		super_sum(1,4,5,6,7) =23
	'''

	total = 0
	for i in args:
		total += i
	return total

print super_sum(10, 20)
print super_sum(1, 4, 5, 6, 7)
a = [10, 40, 60]
print super_sum(*a)

print 
print "_______________________"
print "At least two parameters"
print "________________________"

def super_sum(a,b,*args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g. super_sum(10, 20) =30
		super_sum(10,20,40) =70
		super_sum(1,4,5,6,7) =23
	'''

	total = 0
	for i in args:
		total += i
	return total

print super_sum(10, 20)
print super_sum(1, 4, 5, 6, 7)
a = [10, 40, 60]
print super_sum(*a)

print 
print "_______"
print "Kwargs "
print "_______"

print "Kwargs in a dictionary entry"
print

def hello_again(**kwargs):
	return "I am {}, and I'm {}".format(kwargs['name'], kwargs['age'])

print hello_again(name='Joe', age=20)
print hello_again(age=20, name='Joe')

print
print "Kwargs in a dictionary"
print

joe = {'name': 'Joe', 'age':98}
print hello_again(**joe)
print hello_again(name='Joe', age=98)