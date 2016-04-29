def string_length(data):
	"""
	The function returns the length of the string, or strings in a list
	e.g.
		-['Fairy', 'tale'] ==> return [5, 4]
		-'C-sharp' ==> return [7]
	"""
	b = []

	if type(data) == str:
		b.append(len(data))
		return b
		
	elif type(data) == list:
		for item in data:
			b.append(len(item))
	return b

print string_length("Godson")
print string_length(["Godson", "Joy"])
print string_length(["Godson", "Joy", "Rank"])