from exporter import super_sum, hallo_again, max_min, people

a = [10, 40, -5, 6, 9, 34, 7]
print super_sum, hallo_again, max_min, people 

print hallo_again("Joe", 89)
print super_sum(*a)
print max_min(a)
print hallo_again(*people[0])