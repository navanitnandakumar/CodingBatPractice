def count_code(str):
  count = 0
  for x in range (len(str)-3):
    if str[x] == 'c' and str[x+1] == 'o' and str[x+3] == 'e':
      count += 1
  return count
 
#Expected	Run		
#count_code('aaacodebbb') → 1	1	OK	
#count_code('codexxcode') → 2	2	OK	
#count_code('cozexxcope') → 2	2	OK	
#count_code('cozfxxcope') → 1	1	OK	
#count_code('xxcozeyycop') → 1	1	OK	
#count_code('cozcop') → 0	0	OK	
#count_code('abcxyz') → 0	0	OK	
#count_code('code') → 1	1	OK	
#count_code('ode') → 0	0	OK	
#count_code('c') → 0	0	OK	
#count_code('') → 0	0	OK	
#count_code('AAcodeBBcoleCCccoreDD') → 3	3	OK	
#count_code('AAcodeBBcoleCCccorfDD') → 2	2	OK	
#count_code('coAcodeBcoleccoreDD') → 3	3	OK	
#other tests
#OK
