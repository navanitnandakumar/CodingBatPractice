def end_other(a, b):
  A = a.lower()
  B = b.lower()
  if A.endswith(B) or B.endswith(A):
    return True
  else:
    return False

#Expected	Run		
#end_other('Hiabc', 'abc') → True	True	OK	
#end_other('AbC', 'HiaBc') → True	True	OK	
#end_other('abc', 'abXabc') → True	True	OK	
#end_other('Hiabc', 'abcd') → False	False	OK	
#end_other('Hiabc', 'bc') → True	True	OK	
#end_other('Hiabcx', 'bc') → False	False	OK	
#end_other('abc', 'abc') → True	True	OK	
#end_other('xyz', '12xyz') → True	True	OK	
#end_other('yz', '12xz') → False	False	OK	
#end_other('Z', '12xz') → True	True	OK	
#end_other('12', '12') → True	True	OK	
#end_other('abcXYZ', 'abcDEF') → False	False	OK	
#end_other('ab', 'ab12') → False	False	OK	
#end_other('ab', '12ab') → True	True	OK	
#other tests
#OK
