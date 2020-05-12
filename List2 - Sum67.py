def sum67(nums):
    sum = int(0)
    i = int(0)  
    while i < len(nums):
        if nums[i] == 6:
            while nums[i] != 7:
                i+=1
            i+=1
        if i<len(nums) and nums[i]!=6:  
                sum += nums[i]
                i+=1
    return sum   

#Expected	Run		
#sum67([1, 2, 2]) → 5	5	OK	
#sum67([1, 2, 2, 6, 99, 99, 7]) → 5	5	OK	
#sum67([1, 1, 6, 7, 2]) → 4	4	OK	
#sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) → 2	2	OK	
#sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) → 2	2	OK	
#sum67([2, 7, 6, 2, 6, 7, 2, 7]) → 18	18	OK	
#sum67([2, 7, 6, 2, 6, 2, 7]) → 9	9	OK	
#sum67([1, 6, 7, 7]) → 8	8	OK	
#sum67([6, 7, 1, 6, 7, 7]) → 8	8	OK	
#sum67([6, 8, 1, 6, 7]) → 0	0	OK	
#sum67([]) → 0	0	OK	
#sum67([6, 7, 11]) → 11	11	OK	
#sum67([11, 6, 7, 11]) → 22	22	OK	
#sum67([2, 2, 6, 7, 7]) → 11	11	OK	
#other tests
#OK	
