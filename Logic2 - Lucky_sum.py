def lucky_sum(a, b, c):
    if b == 13 and c == 13:
        return a
    if a == 13:
        return 0   
    if b == 13:
        if a != 13 and c != 13:
            return a
    if c == 13:
        return a + b
    else:
        return a + b + c   
        
#Expected	Run		
#lucky_sum(1, 2, 3) → 6	6	OK	
#lucky_sum(1, 2, 13) → 3	3	OK	
#lucky_sum(1, 13, 3) → 1	1	OK	
#lucky_sum(1, 13, 13) → 1	1	OK	
#lucky_sum(6, 5, 2) → 13	13	OK	
#lucky_sum(13, 2, 3) → 0	0	OK	
#lucky_sum(13, 2, 13) → 0	0	OK	
#lucky_sum(13, 13, 2) → 0	0	OK	
#lucky_sum(9, 4, 13) → 13	13	OK	
#lucky_sum(8, 13, 2) → 8	8	OK	
#lucky_sum(7, 2, 1) → 10	10	OK	
#lucky_sum(3, 3, 13) → 6	6	OK	
#other tests
#OK	        
