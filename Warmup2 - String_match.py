def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1
  return count

#Expected	Run		
#string_match('xxcaazz', 'xxbaaz') → 3	3	OK	
#string_match('abc', 'abc') → 2	2	OK	
#string_match('abc', 'axc') → 0	0	OK	
#string_match('hello', 'he') → 1	1	OK	
#string_match('he', 'hello') → 1	1	OK	
#string_match('h', 'hello') → 0	0	OK	
#string_match('', 'hello') → 0	0	OK	
#string_match('aabbccdd', 'abbbxxd') → 1	1	OK	
#string_match('aaxxaaxx', 'iaxxai') → 3	3	OK	
#string_match('iaxxai', 'aaxxaaxx') → 3	3	OK
