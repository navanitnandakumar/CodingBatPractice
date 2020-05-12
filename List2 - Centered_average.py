def centered_average(nums):
    sum = 0
    total = len(nums)-2
    big = nums.index(max(nums))     
    small = nums.index(min(nums))    
    if big == small:             
        for i in range(len(nums)):      
            if nums[i] == nums[small]:
                big = i             
    for i in range(len(nums)):
        if i != big and i != small:      
            sum = sum + nums[i] 
    if total > 0:
        return sum / total         
    else:
        return sum      

#Expected	Run		
#centered_average([1, 2, 3, 4, 100]) → 3	3	OK	
#centered_average([1, 1, 5, 5, 10, 8, 7]) → 5	5	OK	
#centered_average([-10, -4, -2, -4, -2, 0]) → -3	-3	OK	
#centered_average([5, 3, 4, 6, 2]) → 4	4	OK	
#centered_average([5, 3, 4, 0, 100]) → 4	4	OK	
#centered_average([100, 0, 5, 3, 4]) → 4	4	OK	
#centered_average([4, 0, 100]) → 4	4	OK	
#centered_average([0, 2, 3, 4, 100]) → 3	3	OK	
#centered_average([1, 1, 100]) → 1	1	OK	
#centered_average([7, 7, 7]) → 7	7	OK	
#centered_average([1, 7, 8]) → 7	7	OK	
#centered_average([1, 1, 99, 99]) → 50	50	OK	
#centered_average([1000, 0, 1, 99]) → 50	50	OK	
#centered_average([4, 4, 4, 4, 5]) → 4	4	OK	
#centered_average([4, 4, 4, 1, 5]) → 4	4	OK	
#centered_average([6, 4, 8, 12, 3]) → 6	6	OK	
#other tests
#OK	
