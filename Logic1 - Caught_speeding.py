def caught_speeding(speed, is_birthday):
  if(is_birthday == False):
    if speed >= 61 and speed <= 80:
      return 1
    elif speed >= 81:
      return 2
    else:
      return 0
  elif(is_birthday == True):
    if speed >= 66 and speed <= 85:
      return 1
    elif speed >= 86:
      return 2
    else:
      return 0
      
#Expected	Run		
#caught_speeding(60, False) → 0	0	OK	
#caught_speeding(65, False) → 1	1	OK	
#caught_speeding(65, True) → 0	0	OK	
#caught_speeding(80, False) → 1	1	OK	
#caught_speeding(85, False) → 2	2	OK	
#caught_speeding(85, True) → 1	1	OK	
#caught_speeding(70, False) → 1	1	OK	
#caught_speeding(75, False) → 1	1	OK	
#caught_speeding(75, True) → 1	1	OK	
#caught_speeding(40, False) → 0	0	OK	
#caught_speeding(40, True) → 0	0	OK	
#caught_speeding(90, False) → 2	2	OK	
#other tests
#OK	      
