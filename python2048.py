import os
import random
import copy
import argparse
#Using Argeparse
parser = argparse.ArgumentParser()
parser.add_argument( '--n', type = int, nargs = '?' , default = 4,  help = 'Size of board')
parser.add_argument('--W', type = int , nargs = '?' , default = 2048, help = 'Winning Number' )
arg = parser.parse_args()

n = arg.n
W = arg.W
#Checking Victory Condition
def check(W):
  for a in range(1,100):
    if 2**a == W :
      pass

    else:
      W = 2048
      break
  return W 

#Function to display voard
def display(board,n):
  for i in range(n):
    for j in range(n):
      print(board[i][j],end = "   ")
    print()
    
     
#Function for left movement-1
def mergeleft(row):
  for j in range(n - 1):
    for i in range(n - 1, 0, -1):
      if row[i-1] == 0:
        row[i-1] = row[i]
        row[i] = 0

  for i in range(n - 1):
    if row[i] == row[i + 1]:
      row[i] *= 2
      row[i + 1] = 0

  for i in range(n - 1, 0, -1):
    if row[i - 1] == 0:
      row[i - 1] = row[i]
      row[i] = 0
  return row
 #Left move 
def left(currboard):
  for i in range(n):
    currboard[i] = mergeleft(currboard[i])

  return currboard
#Functions to help with other moves
def reverse(row): 
  new = []
  for i in range(n - 1, -1, -1):
    new.append(row[i])
  return new
 #Right move 
def right(currboard):
  for i in range(n):
    currboard[i] = reverse(currboard[i])
    currboard[i] = mergeleft(currboard[i])
    currboard[i] = reverse(currboard[i])
  return currboard
#Functions to help with other moves
def transpose(currboard):
  for j in range(n):
    for i in range(j, n):
      if not i == j:
        temp = currboard [j][i]
        currboard[j][i] = currboard[i][j]
        currboard[i][j] = temp
  return currboard
#UP move
def up(currboard):
  currboard = transpose(currboard)
  currboard = left(currboard)
  currboard = transpose(currboard)

  return currboard
#Down move
def down(currboard):
  currboard = transpose(currboard)
  currboard = right(currboard)
  currboard = transpose(currboard)

  return currboard
#Spawning random 2s
def Newval():
  rowNum = random.randint(0, n - 1)
  colNum = random.randint(0, n - 1)


  while not board[rowNum][colNum] == 0:
    rowNum = random.randint(0, n - 1)
    colNum = random.randint(0, n - 1)

  board[rowNum][colNum] = 2
#Losing Condition
def loss():
  tempboard1 = copy.deepcopy(board)
  tempboard2 = copy.deepcopy(board)


  tempboard1 = left(tempboard1)
  if tempboard1 == tempboard2:
    tempboard1 = up(tempboard1)
    if tempboard1 == tempboard2:
      tempboard1 = right(tempboard1)
      if tempboard1 == tempboard2:
        tempboard1 = down(tempboard1)
        if tempboard1 == tempboard2:
          return True
  return False

count = 0
#Victory condition
def won(board,n):
  global count
  for i in range(n):
    for j in range(n):
      if board[i][j] == W:
        count = 1
      else:
        count = 0 
  return count

W = check(W)
board = []
for i in range(n):
  row = []
  for j in range(n):
    row.append(0)
  board.append(row)

#Initial two random 2s
numbegin = 2
while numbegin > 0:
  rowNum = random.randint(0, n - 1)
  colNum = random.randint(0, n - 1)


  if board[rowNum][colNum] == 0:
    board[rowNum][colNum] = 2
    numbegin -= 1
  
#Game start
display(board,n)


gameover = False

#Entering the moves
while not gameover:
  print("w is up,a is left,s is down,d is right,no caps")
  move = input("  ")


  validInput = True


  tempBoard = copy.deepcopy(board)

  if move == "d":
    board = right(board)
  elif move == "w":
    board = up(board)
  elif move == "a":
    board = left(board)
  elif move == "s":
    board = down(board)
  else:
    validInput = False
#Game processes
  if not validInput:
    print("Invalid Move,Try again ")
  else:
    if board == tempBoard:
      print("Try different direction")
    else:
       if loss():
          print("GAME OVER")
          gameover = True
          
          
       else:
         won(board,n)
         if count == 1:
           display(board,n)
           print("VICTORY")
           gameover = True

         if count == 0:
           Newval()
           display(board,n)


   

        





