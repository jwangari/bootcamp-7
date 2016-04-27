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