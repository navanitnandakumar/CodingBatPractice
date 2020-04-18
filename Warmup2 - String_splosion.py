def string_splosion(str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
  
#Expected	Run		
#string_splosion('Code') → 'CCoCodCode'	'CCoCodCode'	OK	
#string_splosion('abc') → 'aababc'	'aababc'	OK	
#string_splosion('ab') → 'aab'	'aab'	OK	
#string_splosion('x') → 'x'	'x'	OK	
#string_splosion('fade') → 'ffafadfade'	'ffafadfade'	OK	
#string_splosion('There') → 'TThTheTherThere'	'TThTheTherThere'	OK	
#string_splosion('Kitten') → 'KKiKitKittKitteKitten'	'KKiKitKittKitteKitten'	OK	
#string_splosion('Bye') → 'BByBye'	'BByBye'	OK	
#string_splosion('Good') → 'GGoGooGood'	'GGoGooGood'	OK	
#string_splosion('Bad') → 'BBaBad'	'BBaBad'	OK
