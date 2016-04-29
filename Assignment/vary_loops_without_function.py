"""
Assignment on outputting varying loops
"""
list1 = [(10,20,40), (10,40),(4, 5, 50)]

for item in list1:
	if len(item) == 3:
		print "x: {}, y: {}, z: {}".format(*item)
	elif len(item) == 2:
		print "x: {}, y: {}".format(*item)
	elif len(item) == 1:
		print "x: {}, y: {}".format(item)
	else: 
		print "Invalid length"