def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
    
    #Expected	Run		
#sleep_in(False, False) → True	True	OK	
#sleep_in(True, False) → False	False	OK	
#sleep_in(False, True) → True	True	OK	
#sleep_in(True, True) → True	True	OK	
