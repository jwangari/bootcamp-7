def words(string):
	"""
	The function counts the word occurence in a string
		e.g. For "olly olly in come free"

			olly: 2
			in: 1
			come: 1
			free: 1
	"""
	new_list = string.split()
	string_dict = {}

	for word in new_list:
		if word.isdigit(): 
			word = int(word)

		if word in string_dict:
			string_dict[word] = string_dict[word] + 1
      
		else:
			string_dict[word] = 1
  	return string_dict

print words("Hi hi hi how are : : yah")