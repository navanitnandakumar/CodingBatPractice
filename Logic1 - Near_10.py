def near_ten(num):
    r = num % 10
    if r <= 2 and r >= 0:
        return True
    elif r >= 8 and r <= 9:
        return True
    else:
        return False

#Expected	Run		
#near_ten(12) → True	True	OK	
#near_ten(17) → False	False	OK	
#near_ten(19) → True	True	OK	
#near_ten(31) → True	True	OK	
#near_ten(6) → False	False	OK	
#near_ten(10) → True	True	OK	
#near_ten(11) → True	True	OK	
#near_ten(21) → True	True	OK	
#near_ten(22) → True	True	OK	
#near_ten(23) → False	False	OK	
#near_ten(54) → False	False	OK	
#near_ten(155) → False	False	OK	
#near_ten(158) → True	True	OK	
#near_ten(3) → False	False	OK	
#near_ten(1) → True	True	OK	
#other tests
#OK	
