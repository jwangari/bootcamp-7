

def super_sum(A):
	"""
	Takes a list A, and:
		-Halves every even number
		-Doubles every odd number
	And returns sum of all
	"""
	total = 0
	for item in A:
		if item%2 == 0:
			item=item/2
			total += item
			
		else:
			item=item*2
			total += item 
			
	return total

print super_sum([1,2,3,4,5])
print super_sum([2,3])

