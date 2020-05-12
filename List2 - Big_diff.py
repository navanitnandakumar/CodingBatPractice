def big_diff(nums):
  big = max(i for i in nums)
  small = min(i for i in nums)
  return big-small

#Expected	Run		
#big_diff([10, 3, 5, 6]) → 7	7	OK	
#big_diff([7, 2, 10, 9]) → 8	8	OK	
#big_diff([2, 10, 7, 2]) → 8	8	OK	
#big_diff([2, 10]) → 8	8	OK	
#big_diff([10, 2]) → 8	8	OK	
#big_diff([10, 0]) → 10	10	OK	
#big_diff([2, 3]) → 1	1	OK	
#big_diff([2, 2]) → 0	0	OK	
#big_diff([2]) → 0	0	OK	
#big_diff([5, 1, 6, 1, 9, 9]) → 8	8	OK	
#big_diff([7, 6, 8, 5]) → 3	3	OK	
#big_diff([7, 7, 6, 8, 5, 5, 6]) → 3	3	OK	
#other tests
#OK	
