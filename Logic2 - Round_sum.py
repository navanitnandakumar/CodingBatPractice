def round10(num):
  if num % 10 >= 5:
    newNum = (num/10 + 1)*10
  else:
    newNum = (num/10) * 10
  return newNum

def round_sum(a, b, c):
  return round10(a)+round10(b)+round10(c)
  
#Expected	Run		
#round_sum(16, 17, 18) → 60	60	OK	
#round_sum(12, 13, 14) → 30	30	OK	
#round_sum(6, 4, 4) → 10	10	OK	
#round_sum(4, 6, 5) → 20	20	OK	
#round_sum(4, 4, 6) → 10	10	OK	
#round_sum(9, 4, 4) → 10	10	OK	
#round_sum(0, 0, 1) → 0	0	OK	
#round_sum(0, 9, 0) → 10	10	OK	
#round_sum(10, 10, 19) → 40	40	OK	
#round_sum(20, 30, 40) → 90	90	OK	
#round_sum(45, 21, 30) → 100	100	OK	
#round_sum(23, 11, 26) → 60	60	OK	
#round_sum(23, 24, 25) → 70	70	OK	
#round_sum(25, 24, 25) → 80	80	OK	
#round_sum(23, 24, 29) → 70	70	OK	
#round_sum(11, 24, 36) → 70	70	OK	
#round_sum(24, 36, 32) → 90	90	OK	
#round_sum(14, 12, 26) → 50	50	OK	
#round_sum(12, 10, 24) → 40	40	OK	
#other tests
#OK  
