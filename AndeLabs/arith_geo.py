def arith_geo (A): 
  """
	Check if the array passed is:
	 -arithmetic
	 -geometric
	 -neither arithmetic nor geometric in progression
	 -if the array is empty.

	For arithmetic progressions ==> return Arithmetic
	For geometric progressions ==> return Geometric
	For neither of the above, return -1
	For an empty array, return 0

  """
  if len(A) == 0:
    return 0

  elif is_arithmetic(A):
    return "Arithmetic"

  elif is_geometric(A): 
    return "Geometric"
  
  else:
    return -1

def is_arithmetic(A):
    difference = A[1] - A[0]
    for index in range(len(A)-1):
        if not (A[index + 1] - A[index] == difference):
             return False
    return True

def is_geometric(A):
  ratio = A[1]/float(A[0])
  for index in range(len(A)-1):
    if not (A[index + 1] / float(A[index]) == ratio):
      return False
  return True

print arith_geo([2, 4, 6, 8, 10])
print arith_geo([])
print arith_geo([-128, 64, -32, 16, -8])
print arith_geo([1, 2, 3, 5, 8])

