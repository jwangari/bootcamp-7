def data_type(data=None):
  
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