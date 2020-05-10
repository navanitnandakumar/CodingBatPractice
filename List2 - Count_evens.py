def count_evens(nums):
  count = int(0)
  for i in nums:
    if int(i)%2 == 0:
      count+=1
  return count

#Expected	Run		
#count_evens([2, 1, 2, 3, 4]) → 3	3	OK	
#count_evens([2, 2, 0]) → 3	3	OK	
#count_evens([1, 3, 5]) → 0	0	OK	
#count_evens([]) → 0	0	OK	
#count_evens([11, 9, 0, 1]) → 1	1	OK	
#count_evens([2, 11, 9, 0]) → 2	2	OK	
#count_evens([2]) → 1	1	OK	
#count_evens([2, 5, 12]) → 2	2	OK	
#other tests
#OK	
