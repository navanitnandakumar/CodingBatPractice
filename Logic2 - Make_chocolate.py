def make_chocolate(small, big, goal):
  t = small + (5*big) 
  if t == goal:
    return small       
  if t < goal:   
    return -1
  if big*5 < goal and (goal - big*5) <= small:    
    return goal - (big*5)                       
  else:
    reminder = goal % 5       
    if reminder == small:
      return small 
    if reminder > small:     
      return -1               
    else:
      return reminder  
      
#Expected	Run		
#make_chocolate(4, 1, 9) → 4	4	OK	
#make_chocolate(4, 1, 10) → -1	-1	OK	
#make_chocolate(4, 1, 7) → 2	2	OK	
#make_chocolate(6, 2, 7) → 2	2	OK	
#make_chocolate(4, 1, 5) → 0	0	OK	
#make_chocolate(4, 1, 4) → 4	4	OK	
#make_chocolate(5, 4, 9) → 4	4	OK	
#make_chocolate(9, 3, 18) → 3	3	OK	
#make_chocolate(3, 1, 9) → -1	-1	OK	
#make_chocolate(1, 2, 7) → -1	-1	OK	
#make_chocolate(1, 2, 6) → 1	1	OK	
#make_chocolate(1, 2, 5) → 0	0	OK	
#make_chocolate(6, 1, 10) → 5	5	OK	
#make_chocolate(6, 1, 11) → 6	6	OK	
#make_chocolate(6, 1, 12) → -1	-1	OK	
#make_chocolate(6, 1, 13) → -1	-1	OK	
#make_chocolate(6, 2, 10) → 0	0	OK	
#make_chocolate(6, 2, 11) → 1	1	OK	
#make_chocolate(6, 2, 12) → 2	2	OK	
#make_chocolate(60, 100, 550) → 50	50	OK	
#make_chocolate(1000, 1000000, 5000006) → 6	6	OK	
#make_chocolate(7, 1, 12) → 7	7	OK	
#make_chocolate(7, 1, 13) → -1	-1	OK	
#make_chocolate(7, 2, 13) → 3	3	OK	
#other tests
#OK	      
