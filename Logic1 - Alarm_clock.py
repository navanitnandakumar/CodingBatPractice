def alarm_clock(day, vacation):
  if vacation == True:
    if day in (1,2,3,4,5):
      return "10:00"
    elif day in (0,6):
      return "off"
  elif vacation == False:
    if day in (1,2,3,4,5):
      return "7:00"
    elif day in (0,6):
      return "10:00"
      
#Expected	Run		
#alarm_clock(1, False) → '7:00'	'7:00'	OK	
#alarm_clock(5, False) → '7:00'	'7:00'	OK	
#alarm_clock(0, False) → '10:00'	'10:00'	OK	
#alarm_clock(6, False) → '10:00'	'10:00'	OK	
#alarm_clock(0, True) → 'off'	'off'	OK	
#alarm_clock(6, True) → 'off'	'off'	OK	
#alarm_clock(1, True) → '10:00'	'10:00'	OK	
#alarm_clock(3, True) → '10:00'	'10:00'	OK	
#alarm_clock(5, True) → '10:00'	'10:00'	OK	
#other tests
#OK      
