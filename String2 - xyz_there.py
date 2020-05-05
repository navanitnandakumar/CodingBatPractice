def xyz_there(str):
  return str.count('.xyz') != str.count('xyz')

#Expected	Run		
#xyz_there('abcxyz') → True	True	OK	
#xyz_there('abc.xyz') → False	False	OK	
#xyz_there('xyz.abc') → True	True	OK	
#xyz_there('abcxy') → False	False	OK	
#xyz_there('xyz') → True	True	OK	
#xyz_there('xy') → False	False	OK	
#xyz_there('x') → False	False	OK	
#xyz_there('') → False	False	OK	
#xyz_there('abc.xyzxyz') → True	True	OK	
#xyz_there('abc.xxyz') → True	True	OK	
#xyz_there('.xyz') → False	False	OK	
#xyz_there('12.xyz') → False	False	OK	
#xyz_there('12xyz') → True	True	OK	
#xyz_there('1.xyz.xyz2.xyz') → False	False	OK	
#other tests
#OK	
