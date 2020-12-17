import Print, get

def display():
  Print.clear()
  print()
  Print.yellow('Select your path to find out more:')
  Print.green('\n\t1 - Government')
  Print.green('\n\t2 - ??? - [for you to write]')
  Print.green('\n\t3 - ??? - [for you to write]')
  Print.green('\n\t4 - ??? - [for you to write]')

  return get.number(1) # only 1 story right now, change this number as we add more