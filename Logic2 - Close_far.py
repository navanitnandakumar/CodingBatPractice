def close_far(a, b, c):
  x = abs(a-b)
  y = abs(b-c)
  z = abs(a-c)
  if((x >= 2 and y >= 2)or(x >= 2 and z >= 2)or(y >= 2 and z >= 2)):
    return True
  else:
    return False

#Expected	Run		
#close_far(1, 2, 10) → True	True	OK	
#close_far(1, 2, 3) → False	False	OK	
#close_far(4, 1, 3) → True	True	OK	
#close_far(4, 5, 3) → False	False	OK	
#close_far(4, 3, 5) → False	False	OK	
#close_far(-1, 10, 0) → True	True	OK	
#close_far(0, -1, 10) → True	True	OK	
#close_far(10, 10, 8) → True	True	OK	
#close_far(10, 8, 9) → False	False	OK	
#close_far(8, 9, 10) → False	False	OK	
#close_far(8, 9, 7) → False	False	OK	
#close_far(8, 6, 9) → True	True	OK	
#other tests
#OK	
