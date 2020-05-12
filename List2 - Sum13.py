def sum13(nums):
  sum = int(0)
  for i in range(len(nums)):
    if nums[i] != 13:
      sum+=nums[i]
    elif nums[i] == 13 and i<len(nums)-1:
      nums[i] = nums[i+1] = 0
  return sum
  
#Expected	Run		
#sum13([1, 2, 2, 1]) → 6	6	OK	
#sum13([1, 1]) → 2	2	OK	
#sum13([1, 2, 2, 1, 13]) → 6	6	OK	
#sum13([1, 2, 13, 2, 1, 13]) → 4	4	OK	
#sum13([13, 1, 2, 13, 2, 1, 13]) → 3	3	OK	
#sum13([]) → 0	0	OK	
#sum13([13]) → 0	0	OK	
#sum13([13, 13]) → 0	0	OK	
#sum13([13, 0, 13]) → 0	0	OK	
#sum13([13, 1, 13]) → 0	0	OK	
#sum13([5, 7, 2]) → 14	14	OK	
#sum13([5, 13, 2]) → 5	5	OK	
#sum13([0]) → 0	0	OK	
#sum13([13, 0]) → 0	0	OK	
#other tests
#OK	  
