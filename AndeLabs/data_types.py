def data_type(data=None):
  """
  The function data_type takes one argument. Compare and return results, based on the argument supplied:
    -For strings, return its length.
    -For None return string 'no value'
    -For booleans return the boolean
    -For integers return a string showing how it compares to hundred 
      e.g.  -for 67 return 'less than 100' 
            -for 4034 return 'more than 100' 
            -for equal to 100 as the case may be
    -For lists return the 3rd item OR None if it doesn't exist
  """
  
  if data == None:
    return "no value"
    
  elif type(data) == str:
    return len(data)
        
  elif type(data) == bool:
    return data
    
  elif type(data) == int:
    if data < 100:
      return "less than 100"
      
    elif data > 100:
      return "more than 100" 
      
    elif data == 100:
      return "equal to 100" 
      
  elif type(data) == list:
    if len(data) >= 3:
      return data[2]
      
    else:
      return None

print data_type("Hi how are you")
print data_type()
print data_type(True)
print data_type(10)
print data_type(1000)
print data_type(100)
print data_type([2,3,43,5,3])
print data_type([2,3])
print data_type([2,3,5])