def find_missing(A, B):
	"""
	The function find_missung takes two arrays, all containing positive integers.
	If one of the arrays will have one extra number:
	e.g 
		-[1,2,3] and [1,2,3,4] ==> return 4
		-[4,66,7] and [66,77,7,4] should return 77
	"""

	l_A = len(A)
 	l_B = len(B)

	if l_A == l_B:
		return 0

	else:
		for number in A:
			if number not in B:
				a = number

		for number in B:
			if number not in A:
				a = number
	return a

print find_missing([1,2,3], [1,2,3,4])
print find_missing([4,66,7], [66,77,7,4])
print find_missing([66,77,7,4], [4,66,7])



