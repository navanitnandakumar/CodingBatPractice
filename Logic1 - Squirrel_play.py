def squirrel_play(temp, is_summer):
  if is_summer == True:
    if temp >= 60 and temp <= 100:
      return True
    else:
      return False
  elif temp >= 60 and temp <= 90:
    return True
  else:
    return False
    
#Expected	Run		
#squirrel_play(70, False) → True	True	OK	
#squirrel_play(95, False) → False	False	OK	
#squirrel_play(95, True) → True	True	OK	
#squirrel_play(90, False) → True	True	OK	
#squirrel_play(90, True) → True	True	OK	
#squirrel_play(50, False) → False	False	OK	
#squirrel_play(50, True) → False	False	OK	
#squirrel_play(100, False) → False	False	OK	
#squirrel_play(100, True) → True	True	OK	
#squirrel_play(105, True) → False	False	OK	
#squirrel_play(59, False) → False	False	OK	
#squirrel_play(59, True) → False	False	OK	
#squirrel_play(60, False) → True	True	OK	
#other tests
#OK    
