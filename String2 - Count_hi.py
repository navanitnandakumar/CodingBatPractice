def count_hi(str):
  count= int(0)
  for i in range(len(str)-1):
    if str[i] == 'h' and str[i+1] == 'i':
      count+=1
  return count
  
#Expected	Run		
#count_hi('abc hi ho') → 1	1	OK	
##count_hi('ABChi hi') → 2	2	OK	
#count_hi('hihi') → 2	2	OK	
#count_hi('hiHIhi') → 2	2	OK	
#count_hi('') → 0	0	OK	
#count_hi('h') → 0	0	OK	
#count_hi('hi') → 1	1	OK	
#count_hi('Hi is no HI on ahI') → 0	0	OK	
#count_hi('hiho not HOHIhi') → 2	2	OK	
#other tests
#OK
