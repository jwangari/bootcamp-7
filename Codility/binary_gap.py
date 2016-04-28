
def solution(N):
	b = []
	new_list = []
	
	while N != 0:
		x = N%2
		b.append(x)
		N = N/2
	
	new_list = b [::-1]
	count = 0

	for item in new_list:
		if item == 1:
			



print solution(9)
print solution(529)

