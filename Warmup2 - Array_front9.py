def array_front9(nums):
  t = 1
  found = False
  for num in (nums):
    if t<5:
      if num == 9:
        return True
        found = True
    t+=1
  if not found:
    return False
    
#Expected	Run		
#array_front9([1, 2, 9, 3, 4]) → True	True	OK	
#array_front9([1, 2, 3, 4, 9]) → False	False	OK	
#array_front9([1, 2, 3, 4, 5]) → False	False	OK	
#array_front9([9, 2, 3]) → True	True	OK	
#array_front9([1, 9, 9]) → True	True	OK	
#array_front9([1, 2, 3]) → False	False	OK	
#array_front9([1, 9]) → True	True	OK	
#array_front9([5, 5]) → False	False	OK	
#array_front9([2]) → False	False	OK	
#array_front9([9]) → True	True	OK	
#array_front9([]) → False	False	OK	
#array_front9([3, 9, 2, 3, 3]) → True	True	OK	
