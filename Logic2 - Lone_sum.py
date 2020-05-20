def lone_sum(a, b, c):
    if a == b and b == c:
        return 0
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c
        
#Expected	Run		
#lone_sum(1, 2, 3) → 6	6	OK	
#lone_sum(3, 2, 3) → 2	2	OK	
#lone_sum(3, 3, 3) → 0	0	OK	
#lone_sum(9, 2, 2) → 9	9	OK	
#lone_sum(2, 2, 9) → 9	9	OK	
#lone_sum(2, 9, 2) → 9	9	OK	
#lone_sum(2, 9, 3) → 14	14	OK	
#lone_sum(4, 2, 3) → 9	9	OK	
#lone_sum(1, 3, 1) → 3	3	OK	
#other tests
#OK	
