def monkey_trouble(a_smile, b_smile):
  if( (a_smile and b_smile) or (not a_smile and not b_smile)):
    return True
  else:
    return False
    
    #Expected	Run		
#monkey_trouble(True, True) → True	True	OK	
#monkey_trouble(False, False) → True	True	OK	
#monkey_trouble(True, False) → False	False	OK	
#monkey_trouble(False, True) → False	False	OK	
