def reverse_string(string):
	
	b = []

	for item in range(len(string)-1, -1, -1):
		b.append(string[item])
		str1 = "".join(b)

	if string == "":
	  return None
	elif b == list(string):
		return True
	else:
		return str1
print reverse_string("civic")
print reverse_string("books")

