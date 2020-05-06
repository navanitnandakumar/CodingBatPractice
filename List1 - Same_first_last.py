def same_first_last(nums):
  if len(nums)>1:
    return nums[0] == nums[-1]
  elif len(nums) == 1:
    return True
  elif len(nums) == 0:
    return False
    
#Expected	Run		
#same_first_last([1, 2, 3]) → False	False	OK	
#same_first_last([1, 2, 3, 1]) → True	True	OK	
#same_first_last([1, 2, 1]) → True	True	OK	
#same_first_last([7]) → True	True	OK	
#same_first_last([]) → False	False	OK	
#same_first_last([1, 2, 3, 4, 5, 1]) → True	True	OK	
#same_first_last([1, 2, 3, 4, 5, 13]) → False	False	OK	
#same_first_last([13, 2, 3, 4, 5, 13]) → True	True	OK	
#same_first_last([7, 7]) → True	True	OK	
#other tests
#OK
