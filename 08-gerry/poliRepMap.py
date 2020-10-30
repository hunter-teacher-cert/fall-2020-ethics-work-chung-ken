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

# Check that every cell "voted"
print("How the state voted this time:")
for i in range(ROWS):
  print("District " + str(i+1) + ":", end = ' ')
  print(state[i])
