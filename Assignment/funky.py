def funky(a, b):
    """concatenating data types/data structures"""
    if type(a) and type(b) == str:
        return a + b
    elif (type(a) and type(b) == int) or (type(a) and type(b)== float):
        return a + b
    elif type(a) and type(b) == list:
        return a + b
    elif type(a) and type(b) == dict:
        new_dict = dict(a.items() + b.items())
        return new_dict
    else:
        return 'Invalid Input'

print funky(1, 4.2)
print funky(1, 2)
print funky('mama', 'papa')

print funky(2.2, 1.0)
print funky([1,2,3], ['me', 'my'])
print funky({1:'one', 2:'two', 'five':5}, {'three':3, 'four':4})

