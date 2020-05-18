
import random
import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( '--n', type = int, nargs = '?' , default = 4,  help = 'Size of board')
parser.add_argument('--W', type = int , nargs = '?' , default = 2048, help = 'Winning Number' )
arg = parser.parse_args()

n = arg.n
W = arg.W

def check(W):
  for a in range(1,100):
    if 2**a == W :
      pass

    else:
      W = 2048
      break
  return W 


def display(board,n):
  for i in range(n):
    for j in range(n):
      print(board[i][j],end = " ")
    print()
    
     

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
  
def left(currboard):
  for i in range(n):
    currboard[i] = mergeleft(currboard[i])

  return currboard

def reverse(row): 
  new = []
  for i in range(n - 1, -1, -1):
    new.append(row[i])
  return new
  
def right(currboard):
  for i in range(n):
    currboard[i] = reverse(currboard[i])
    currboard[i] = mergeleft(currboard[i])
    currboard[i] = reverse(currboard[i])
  return currboard

def transpose(currboard):
  for j in range(n):
    for i in range(j, n):
      if not i == j:
        temp = currboard [j][i]
        currboard[j][i] = currboard[i][j]
        currboard[i][j] = temp
  return currboard

def up(currboard):
  currboard = transpose(currboard)
  currboard = left(currboard)
  currboard = transpose(currboard)

  return currboard

def down(currboard):
  currboard = transpose(currboard)
  currboard = right(currboard)
  currboard = transpose(currboard)

  return currboard

def Newval():
  rowNum = random.randint(0, n - 1)
  colNum = random.randint(0, n - 1)


  while not board[rowNum][colNum] == 0:
    rowNum = random.randint(0, n - 1)
    colNum = random.randint(0, n - 1)

  board[rowNum][colNum] = 2

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

def won(board,n):
  for i in range(n):
    for j in range(n):
      if board[i][j] == W:
        count = 1
      else:
        count = 0 
  return count
count = 0
W = check(W)
board = []
for i in range(n):
  row = []
  for j in range(n):
    row.append(0)
  board.append(row)


numbegin = 2
while numbegin > 0:
  rowNum = random.randint(0, n - 1)
  colNum = random.randint(0, n - 1)


  if board[rowNum][colNum] == 0:
    board[rowNum][colNum] = 2
    numbegin -= 1
  

display(board,n)


gameover = False


while not gameover:
  move = input("Which direction to move?")


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

  if not validInput:
    print("Invalid Move,Try again ")
  else:
    if board == tempBoard:
      print("Try different direction")
    else:
      won(board,n)
      if count == 1:
        display(board,n)
        print("VICTORY")
        gameover = True

      if count == 0:
        if loss():
          print("GAME OVER")
          gameover = True

        else:
          Newval()
          display(board,n)


   

        





