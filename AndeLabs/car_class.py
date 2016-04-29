class Car:
	"""
	Car class instantiates various vehicles.

	It takes in arguments that depict:
		- the type
		- model
		- name of the vehicle (provided they are set)
	"""
	def __init__(self, type1='', model='', name=''):
		self.type = type1
		self.model = model
		self.name = name

		if not self.name:
			self.name = "General"
		if not self.model:
			self.model = "GM"
	# def car_properties(self):
	# 	self.name = name
	# 	self.model = model
	def num_of_doors(self):
		if self.type1 != "porshe" or "koenigsegg":
			return 4
		return 2
	def num_of_wheels(self):
		if self.type1 != "trailer":
			return 4
		return 8
	def is_saloon(self):



honda = Car("Honda")
toyota = Car("Toyota", "Corolla")
porshe = Car("Porshe")

print toyota.num_of_doors
print toyota.model
print porshe.num_of_doors