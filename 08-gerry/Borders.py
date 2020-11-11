# There are 2 functions in here:
# 1) addColor(num, i=None)
# 2) createDistrictBorders(vote, map)


####################################
##    Add color to party votes    ##
####################################
def addColor(num, i=None):
  colorized = ""
  if i == None:
  #add color to a 0, 1, etc.
    if num == 0:
      colorized += "\u001b[31m"
    elif num == 1:
      colorized += "\u001b[36m"
    else:
      colorized += "\u001b[32m"
  else:
  #add a color i to a number num
    if i == 0:
      colorized += "\u001b[31m"
    elif i == 1:
      colorized += "\u001b[36m"
    else:
      colorized += "\u001b[32m"
  colorized += str(num) + "\u001b[0m"
  return colorized
####################################
##        End of addColor         ##
####################################


####################################
##    Create District Borders     ##
####################################
def createDistrictBorders(vote, map): 

  output = ""
  
  # terminal border lines
  # ajejb  ┌─┬─┐
  # k k k  │ │ │
  # fjijg  ├─┼─┤
  # k k k  │ │ │
  # cjhjd  └─┴─┘
  
  a = chr(0x250c) #upper-left corner
  b = chr(0x2510) #upper-right corner
  c = chr(0x2514) #lower-left corner
  d = chr(0x2518) #lower-right corner
  e = chr(0x252c) #top T
  f = chr(0x251c) #left T
  g = chr(0x2524) #right T
  h = chr(0x2534) #bottom T
  i = chr(0x253c) #middle plus, +
  j = chr(0x2500) #horizontal dash
  k = chr(0x2502) #vertical dash

  #top rows
  row1String = a  #border row
  row2String = k  #vote row
  for m in range(len(map[0])-1):
    row2String += " " + addColor(vote[0][m]) + " "
    row1String += j*3
    if (map[0][m] == map[0][m+1]):
      row2String += " "
      row1String += j
    else:
      row2String += k
      row1String += e
  row2String += " " + addColor(vote[0][len(map[0])-1]) + " " + k
  row1String += j*3 + b
  output += row1String + '\n' + row2String + '\n'

  #middle rows
  for m in range(1,len(map)):
    if (map[m][0] == map[m-1][0]):
      row1String = k
    else:
      row1String = f
    row2String = k
    for n in range(len(map[m])-1):
      row2String += " " + addColor(vote[m][n]) + " "
      if (map[m][n] == map[m-1][n]):
        row1String += "   "
        if (map[m][n] == map[m][n+1]):
          row2String += " "
          if (map[m][n+1] == map[m-1][n+1]):
            row1String += " "
          else:
            row1String += c
        else:
          row2String += k
          if (map[m][n+1] == map[m-1][n+1]):
            row1String += k
          else:
            if (map[m-1][n] == map[m-1][n+1]):
              row1String += a
            else:
              row1String += f
      else:
        row1String += j*3
        if (map[m][n] == map[m][n+1]):
          row2String += " "
          if (map[m][n+1] == map[m-1][n+1]):
            row1String += d
          else:
            if (map[m-1][n] == map[m-1][n+1]):
              row1String += j
            else:
              row1String += h
        else:
          row2String += k
          if (map[m][n+1] == map[m-1][n+1]):
            if (map[m-1][n] == map[m-1][n+1]):
              row1String += b
            else:
              row1String += g
          else:
            if (map[m-1][n] == map[m-1][n+1]):
              row1String += e
            else:
              row1String += i
    row2String += " " + addColor(vote[m][len(map[m])-1]) + " " + k
    if (map[m][len(map[m])-1] == map[m-1][len(map[m])-1]):
      row1String += "   " + k
    else:
      row1String += j*3 + g
    output += row1String + '\n' + row2String + '\n'
  
  #bottom row
  row1String = c
  n = len(map)-1
  for m in range(len(map[n])-1):
    if (map[n][m] == map[n][m+1]):
      row1String += j*3 + j
    else:
      row1String += j*3 + h
  row1String += j*3 + d
  output += row1String + '\n'
  return output
####################################
##    END OF DISTRICT BORDERS     ##
####################################

