def string_bits(str):
  final = ""
  for i in range(len(str)):
    if i % 2 == 0:
      final+=str[i]
  return final
      
#Expected	Run		
#string_bits('Hello') → 'Hlo'	'Hlo'	OK	
#string_bits('Hi') → 'H'	'H'	OK	
#string_bits('Heeololeo') → 'Hello'	'Hello'	OK	
#string_bits('HiHiHi') → 'HHH'	'HHH'	OK	
#string_bits('') → ''	''	OK	
#string_bits('Greetings') → 'Getns'	'Getns'	OK	
#string_bits('Chocoate') → 'Coot'	'Coot'	OK	
#string_bits('pi') → 'p'	'p'	OK	
#string_bits('Hello Kitten') → 'HloKte'	'HloKte'	OK	
#string_bits('hxaxpxpxy') → 'happy'	'happy'	OK	      
