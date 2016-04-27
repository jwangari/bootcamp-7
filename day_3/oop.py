# PEP8

class Person:
	# class variable: access use class name
	people_count = 0
	def __init__(self, name, age):
		#instance variables access use self
		self.name = name
		self.age = age
		Person.people_count += 1

	def __repr__(self,):
		return "<{}, {}>".format(self.name, self.age)
	
	def say_hello(self,):
		return "Hello, I'm {} and {} y/o".format(self.name, self.age)

p = Person('Joe', 23)
p2 = Person('Jane', 30)
p3 = Person('George', 65)

a = [('Jane', 20), ('Joy', 22),
		('Jee', 35), ('Joe', 56)]
b = []

for name, age in a:
	person = Person(name, age)
	b.append(person)
print b

for person in b:
	print person.say_hello()

print Person.people_count
#print p2.people_count
print p.name, p.age
print p.say_hello()