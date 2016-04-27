list1 = [10, 3, 2, 56, -70]

for item in list1:
	print item

print 
print "__________"
print "In Reverse"
print "__________"
print 

i = len(list1)

while i > 0:
	print list1[i - 1]
	i -= 1

#print list1[-1]

print 
print "______________________"
print "In Reverse using range"
print "______________________"
print 
'''

This might help understand range(len(list1) - 1, -1, -1)
a = range(len(list1), 0, -1)
b = range(len(list1), -1, -1)

print a
print b
'''
for item in range(len(list1) - 1, -1, -1):
	print list1[item]

print 
print "______________"
print "Advanced Loops"
print "______________"
print 

list2 = [(2,4), (3,1), (1,2)]
'''
x:2, y:4

'''

print 
print "Using item-value combo"

for item,value in list2:
	print "x: {}, y: {}".format(item,value)

print 
print "Unpacking item"

for item in list2:
	print "x: {}, y: {}".format(*item)

'''
Assignment:
List = [(10,20,40), (10,40), (4,5,50)]

Output: 
x: 10 y: 20 z:40
x: 10 y:40
'''