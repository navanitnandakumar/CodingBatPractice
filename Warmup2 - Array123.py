def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
  
#Expected	Run		
#array123([1, 1, 2, 3, 1]) → True	True	OK	
#array123([1, 1, 2, 4, 1]) → False	False	OK	
#array123([1, 1, 2, 1, 2, 3]) → True	True	OK	
#array123([1, 1, 2, 1, 2, 1]) → False	False	OK	
#array123([1, 2, 3, 1, 2, 3]) → True	True	OK	
#array123([1, 2, 3]) → True	True	OK	
#array123([1, 1, 1]) → False	False	OK	
#array123([1, 2]) → False	False	OK	
#array123([1]) → False	False	OK	
#array123([]) → False	False	OK	
