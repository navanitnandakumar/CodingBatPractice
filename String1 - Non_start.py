def non_start(a, b):
  answer = a[1:]+b[1:]
  return answer

#Expected	Run		
#non_start('Hello', 'There') → 'ellohere'	'ellohere'	OK	
#non_start('java', 'code') → 'avaode'	'avaode'	OK	
#non_start('shotl', 'java') → 'hotlava'	'hotlava'	OK	
#non_start('ab', 'xy') → 'by'	'by'	OK	
#non_start('ab', 'x') → 'b'	'b'	OK	
#non_start('x', 'ac') → 'c'	'c'	OK	
#non_start('a', 'x') → ''	''	OK	
#non_start('kit', 'kat') → 'itat'	'itat'	OK	
#non_start('mart', 'dart') → 'artart'	'artart'	OK	
#other tests
#OK
