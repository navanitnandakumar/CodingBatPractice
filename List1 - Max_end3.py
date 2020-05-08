def max_end3(nums):
  answer = [max(nums[0],nums[-1]),max(nums[0],nums[-1]),max(nums[0],nums[-1])]
  return answer

#Expected	Run		
#max_end3([1, 2, 3]) → [3, 3, 3]	[3, 3, 3]	OK	
#max_end3([11, 5, 9]) → [11, 11, 11]	[11, 11, 11]	OK	
#max_end3([2, 11, 3]) → [3, 3, 3]	[3, 3, 3]	OK	
#max_end3([11, 3, 3]) → [11, 11, 11]	[11, 11, 11]	OK	
#max_end3([3, 11, 11]) → [11, 11, 11]	[11, 11, 11]	OK	
#max_end3([2, 2, 2]) → [2, 2, 2]	[2, 2, 2]	OK	
#max_end3([2, 11, 2]) → [2, 2, 2]	[2, 2, 2]	OK	
#max_end3([0, 0, 1]) → [1, 1, 1]	[1, 1, 1]	OK	
#other tests
#OK
