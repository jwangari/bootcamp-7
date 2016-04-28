def word_count(string):
	list=string.split()
	#new_list=set(list)
	my_dict={}
	for item in list:
		my_dict[item] = list.count(item)
	return my_dict		
# the one that works with one error
# def words(word):
#   string_list = word.split()
#   string_dict = {}

#   for word in string_list:
#     if word in string_dict:
#       string_dict[word] = string_dict[word] + 1
#       continue
#     else:
#       string_dict[word] = 1
#   return string_dict