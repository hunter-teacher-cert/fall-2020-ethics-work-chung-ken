def number(max):
  choice = 0
  while choice < 1 or choice > max:
    choice = input('\n\nEnter a number 1-' + str(max) + ': ')
    try:
      choice = int(choice)
    except:
      print('\tNot a valid number.')
      choice = 0
      continue
  return choice-1