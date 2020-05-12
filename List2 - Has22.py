def has22(nums):
  flag = False
  for i in range(len(nums)):
    if nums[i] == 2 and i+1 < len(nums) and nums[i+1] == 2:
      flag = True
  return flag
  
#Expected	Run		
#has22([1, 2, 2]) → True	True	OK	
#has22([1, 2, 1, 2]) → False	False	OK	
#has22([2, 1, 2]) → False	False	OK	
#has22([2, 2, 1, 2]) → True	True	OK	
#has22([1, 3, 2]) → False	False	OK	
#has22([1, 3, 2, 2]) → True	True	OK	
#has22([2, 3, 2, 2]) → True	True	OK	
#has22([4, 2, 4, 2, 2, 5]) → True	True	OK	
#has22([1, 2]) → False	False	OK	
#has22([2, 2]) → True	True	OK	
#has22([2]) → False	False	OK	
#has22([]) → False	False	OK	
#has22([3, 3, 2, 2]) → True	True	OK	
#has22([5, 2, 5, 2]) → False	False	OK	
#other tests
#OK	  
