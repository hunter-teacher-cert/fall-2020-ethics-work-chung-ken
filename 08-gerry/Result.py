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
  count[6][0] = sum0  #total votes for 0
  count[6][1] = sum1  #total votes for 1
  count[7][0] = win0  #district wins for 0
  count[7][1] = win1  #district wins for 1
  return count
####################################
##    End of checkWin function    ##
####################################

