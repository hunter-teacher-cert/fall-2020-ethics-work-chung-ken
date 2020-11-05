'''
 Start: Thursday, October 29, 2020
 End: 

 Assignment: Computational Explorations of Political Representation

 Objectives:
 1) Create a state that is a 6x3 grid of cells.
 2) What is your state's name? Lin-o-eL
 3) Each cell is inhabited entirely by citizens who vote '1' XOR citizens who vote '0'.
 4) The program should be able to:
    a) Randomly populate each cell with a 1 or 0.
    b) Display a generated configuration.
    c) Divide your state into 6 "districts":
      i) A district is a list of coordinate pairs, where each pair represents a member cell.
      ii) A district must be comprised of adjacent cells.
    d) Primary goal: ensure each cell is in a district.
    e) Secondary goal: balance district sizes.
'''
import random

# Set the state size
ROWS = 6
COLS = 3

# Create the state in a 2D array populated with random 1s and 0s
state = []
for i in range(ROWS):
  row = []
  for j in range(COLS):
    row.append(random.randint(0,1))
  state.append(row)

#####################################
##         Create Districs         ##
#####################################
districtMap = [];
if (False):
#simple distric map
  for i in range(1,ROWS+1):
    row = []
    for j in range(COLS):
      row.append(i)
    districtMap.append(row)
else:
#create random district shapes
  districtMap.append([1,1,2])
  districtMap.append([3,1,2])
  districtMap.append([3,3,2])
  districtMap.append([4,4,4])
  districtMap.append([5,5,6])
  districtMap.append([5,6,6])


# Look at original district layout
print("\nDISTRICT MAP:")
for i in range(ROWS):
  print(districtMap[i])

# Check how every cell "voted"
print("\nVOTES BY REGION:")
for i in range(ROWS):
  print(state[i])

####################################
##    Add color to party votes    ##
####################################
def addColor(num, i=None):
  colorized = ""
  if i == None:
    if num == 0:
      colorized += "\u001b[31m"
    elif num == 1:
      colorized += "\u001b[36m"
    else:
      colorized += "\u001b[32m"
  else:
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
            row1String += a
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

####################################
##  Check who won each district   ##
####################################
def checkWin(vote, map):
  count = []
  for i in range(6+2):
    row = []
    for j in range(2+1):
      row.append(0)
    count.append(row)
  for i in range(len(map)):
    for j in range(len(map[i])):
      count[map[i][j]-1][vote[i][j]] += 1
  #row 6 will contain the total votes
  #row 7 will contain the district wins
  #col 2 indicates who won that district
  sum0 = 0
  sum1 = 0
  win0 = 0
  win1 = 0
  for i in range(len(map)):
    sum0 += count[i][0]
    sum1 += count[i][1]
    if count[i][0] > count[i][1]:
      count[i][2] = 0
      win0 += 1
    elif count[i][1] > count[i][0]:
      count[i][2] = 1
      win1 += 1
    else:
      count[i][2]=-1
  count[6][0] = sum0
  count[6][1] = sum1
  count[7][0] = win0
  count[7][1] = win1
  return count
####################################
##    End of checkWin function    ##
####################################


print('\n' + createDistrictBorders(state, districtMap))

results = checkWin(state, districtMap)

print("Popular Vote:")
print("Rep: \033[31m%.1f\033[0m%%,  Dem: \033[36m%.1f\033[0m%%" %(results[6][0]*100/(ROWS*COLS), results[6][1]*100/(ROWS*COLS)))

shout = ""
if results[7][0] > results[7][1]:
  shout += "\033[31;1;4mRepublicans Win!\033[0m"
elif results[7][1] > results[7][0]:
  shout += "\033[36;1;4mDeomcrats Win!\033[0m"
else:
  shout += "\033[32;1;4mIt's a tie!\033[0m"
print("\nBy District -", shout)
print("Reps won", addColor(results[7][0],0), "districts")
print("Dems won", addColor(results[7][1],1), "districts")