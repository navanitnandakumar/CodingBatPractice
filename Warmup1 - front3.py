def front3(str):
  if(len(str)<4):
    return(str+str+str)
  
  else:
    new = str[0]+str[1]+str[2]
    return(new+new+new)
    
#Expected	Run		
#front3('Java') → 'JavJavJav'	'JavJavJav'	OK	
#front3('Chocolate') → 'ChoChoCho'	'ChoChoCho'	OK	
#front3('abc') → 'abcabcabc'	'abcabcabc'	OK	
#front3('abcXYZ') → 'abcabcabc'	'abcabcabc'	OK	
#front3('ab') → 'ababab'	'ababab'	OK	
#front3('a') → 'aaa'	'aaa'	OK	
#front3('') → ''	''	OK	
