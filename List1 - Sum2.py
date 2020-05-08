def sum2(nums):
  sum_list = int(0)
  if len(nums)>=2:
    sum_list = nums[0]+nums[1]
  if len(nums)<2 and len(nums)>0:
    sum_list = sum(nums)
  return sum_list

#Expected	Run		
#sum2([1, 2, 3]) → 3	3	OK	
#sum2([1, 1]) → 2	2	OK	
#sum2([1, 1, 1, 1]) → 2	2	OK	
#sum2([1, 2]) → 3	3	OK	
#sum2([1]) → 1	1	OK	
#sum2([]) → 0	0	OK	
#sum2([4, 5, 6]) → 9	9	OK	
#sum2([4]) → 4	4	OK	
#other tests
#OK	
