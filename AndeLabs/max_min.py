def max_min(A):
	"""
	Answer should be returned in an array containing the min and max number, respectively.
	"""
	x = min(A)
	y = max(A)

	if x == y:
		return [len(A)]
	else:
		return [x,y]

print max_min([1, 2, 3, 4])