def vary_loops(*args):
	for item in args:
		if len(item) == 1:
			for x in item:
				result = "x: {}".format(x)
			return result

		elif len(item) == 2:
			for x, y in item:
				result = "x: {}, y:{}".format(x, y)
			return result

		elif len(item) == 3:
			for x, y, z in item:
				result = "x: {}, y:{}, z:{}".format(x, y, z)

			return result
	
print vary_loops([(10,20,40), (23,45), (23,45,67)])
 

 	
 		