def max_min(A):
  x = min(A)
  y = max(A)
  
  if x == y:
    return [len(A)]
  else:
    return [x,y]

print max_min([1, 2, 3, 4])