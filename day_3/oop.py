from person import Person
from kenyan import Kenyan
# PEP8

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

k = Kenyan('Miguna', 23)
#k.probe(True)
print "Is {} corrupt?\n {}".format(k.name, k.is_corrupt())
print k.say_hello()