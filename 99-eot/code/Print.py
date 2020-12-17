def clear():
  print('\033[2J\033[H')

def red(txt):
  print('\033[31m', end='')
  print(txt, end='')
  print('\033[0m')

def green(txt):
  print('\033[32m', end='')
  print(txt, end='')
  print('\033[0m')

def yellow(txt):
  print('\033[38;2;255;255;0m', end='')
  print(txt, end='')
  print('\033[0m')

def pink(txt):
  print('\033[35m', end='')
  print(txt, end='')
  print('\033[0m')

def cyan(txt):
  print('\033[96m', end='')
  print(txt, end='')
  print('\033[0m')

def bold(txt):
  return '\033[1m' + txt + '\033[0m'

def under(txt):
  return '\033[4m' + txt + '\033[0m'

def bgw(txt):
  return '\033[100m' + txt + '\033[0m'

def bgp(txt):
  return '\033[105m' + txt + '\033[0m'

def bgo(txt):
  return '\033[101m' + txt + '\033[0m'

def redf(txt):
  return '\033[31m' + txt + '\033[0m'

def greenf(txt):
  return '\033[32m' + txt + '\033[0m'

def yellowf(txt):
  return '\033[38;2;255;255;0m' + txt + '\033[0m'

def pinkf(txt):
  return '\033[35m' + txt + '\033[0m'
  
def cyanf(txt):
  return '\033[38;2;0;255;255m' + txt + '\033[0m'