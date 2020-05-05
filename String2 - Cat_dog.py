def cat_dog(str):
  cat_count = int(0)
  dog_count = int(0)
  cat_count = str.count("cat")
  dog_count = str.count("dog")
  if cat_count == dog_count:
    return True
  else:
    return False
  
#Expected	Run		
#cat_dog('catdog') → True	True	OK	
#cat_dog('catcat') → False	False	OK	
#cat_dog('1cat1cadodog') → True	True	OK	
#cat_dog('catxxdogxxxdog') → False	False	OK	
#cat_dog('catxdogxdogxcat') → True	True	OK	
#cat_dog('catxdogxdogxca') → False	False	OK	
#cat_dog('dogdogcat') → False	False	OK	
#cat_dog('dogogcat') → True	True	OK	
#cat_dog('dog') → False	False	OK	
#cat_dog('cat') → False	False	OK	
#cat_dog('ca') → True	True	OK	
#cat_dog('c') → True	True	OK	
#cat_dog('') → True	True	OK	
#other tests
#OK	
