def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result
  
  #Expected	Run		
#front_times('Chocolate', 2) → 'ChoCho'	'ChoCho'	OK	
#front_times('Chocolate', 3) → 'ChoChoCho'	'ChoChoCho'	OK	
#front_times('Abc', 3) → 'AbcAbcAbc'	'AbcAbcAbc'	OK	
#front_times('Ab', 4) → 'AbAbAbAb'	'AbAbAbAb'	OK	
#front_times('A', 4) → 'AAAA'	'AAAA'	OK	
#front_times('', 4) → ''	''	OK	
#front_times('Abc', 0) → ''	''	OK	
