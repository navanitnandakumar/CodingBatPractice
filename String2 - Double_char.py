def double_char(str):
  result = []
  for x in str:
    result.append(x)
    result.append(x)
  return ''.join(result)

#Expected	Run		
#double_char('The') → 'TThhee'	'TThhee'	OK	
#double_char('AAbb') → 'AAAAbbbb'	'AAAAbbbb'	OK	
#double_char('Hi-There') → 'HHii--TThheerree'	'HHii--TThheerree'	OK	
#double_char('Word!') → 'WWoorrdd!!'	'WWoorrdd!!'	OK	
#double_char('!!') → '!!!!'	'!!!!'	OK	
#double_char('') → ''	''	OK	
#double_char('a') → 'aa'	'aa'	OK	
#double_char('.') → '..'	'..'	OK	
#double_char('aa') → 'aaaa'	'aaaa'	OK	
#other tests
#OK
