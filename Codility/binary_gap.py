def solution(N):
	"""
	Returns the number passed into the argument as a binary list
	"""
	b = []
	new_list = []
	
	while N != 0:
		x = N%2
		b.append(x)
		N = N/2
	
	new_list = b [::-1]
	count = 0

	return new_list

def solution1(N):
	"""
	Returns the binary gap
	"""
	current_gap = 0
	max_gap = 0

	if N > 0 and N % 2 == 0:
		N //= 2

	while N > 0:
		reminder = N % 2
		if reminder == 0:
			current_gap += 1
		else:
			if current_gap != 0:
				max_gap = max(current_gap, max_gap)
				current_gap = 0
		N //= 2
	return max_gap

print solution(9)
print solution(529)
print solution1(9)
print solution1(529)

