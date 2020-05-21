def fix_teen(n):
  teen = False
  if n >= 13 and n <= 14:
    teen = True
  elif n >= 17 and n <= 19:
    teen = True
  return teen
 
def no_teen_sum(a, b, c):
  if fix_teen(a):
    a = 0
  if fix_teen(b):
    b = 0
  if fix_teen(c):
    c = 0
  return a+b+c
  
#Expected	Run		
#no_teen_sum(1, 2, 3) → 6	6	OK	
#no_teen_sum(2, 13, 1) → 3	3	OK	
#no_teen_sum(2, 1, 14) → 3	3	OK	
#no_teen_sum(2, 1, 15) → 18	18	OK	
#no_teen_sum(2, 1, 16) → 19	19	OK	
#no_teen_sum(2, 1, 17) → 3	3	OK	
#no_teen_sum(17, 1, 2) → 3	3	OK	
#no_teen_sum(2, 15, 2) → 19	19	OK	
#no_teen_sum(16, 17, 18) → 16	16	OK	
#no_teen_sum(17, 18, 19) → 0	0	OK	
#no_teen_sum(15, 16, 1) → 32	32	OK	
#no_teen_sum(15, 15, 19) → 30	30	OK	
#no_teen_sum(15, 19, 16) → 31	31	OK	
#no_teen_sum(5, 17, 18) → 5	5	OK	
#no_teen_sum(17, 18, 16) → 16	16	OK	
#no_teen_sum(17, 19, 18) → 0	0	OK	
#other tests
#OK	  
