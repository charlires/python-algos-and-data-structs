
# The Tron Problem
# Greetings future Episource employee! You have been "randomly" selected to participate in the 11th annual Tron games!
# Don't worry, you won't be actually playing the games. You'll be judging the battles after the fact!
# Let me take a quick second to brief you on the Tron Standard Rules(TSRs).

 

# 1) The game is played on a standard 10x10 board
# 2) Player 1 starts on position 0x0 (top left corner). Player 2 starts on position 9x9 (bottom right corner).
# 3) At each turn, a player may move up, down, left, or right on the board.
     #  These steps are held in an array and take the form 'u', 'd', 'l', and 'r' respectively.
# 4) If a player crosses a previous path of another player, including themselves, they are eliminated.
# 5) If a player lands on the same space as another player on the same turn, both players are eliminated and the match is declared a draw.
# 6) If a player moves off the board, into the vast cyber nothingness, they are eliminated.
# 7) If there is only one player left at the end of a turn, that player wins no matter if they have more moves or not.
# 8) If the match has ended and there is more than one player still active, the match is declared a draw.
# 9) If both players are eliminated on the same turn, the match is declared a draw.

# input:
# player1Moves = ['r', 'd', 'd', 'r', 'r', 'r', 'l', 'l', 'l', 'd', 'd', 'd', 'l', 'd', 'd', 'd', 'd', 'r']
# player2Moves = ['u', 'l', 'l', 'u', 'l', 'l', 'u', 'l', 'l', 'd', 'd', 'l', 'l', 'u', 'u', 'r', 'u', 'l']
# output: “Player 2 wins” … (because player 1 runs into their own path)

 

# input:
# player1Moves = ['d', 'd', 'r', 'r', 'r', 'u', 'r', 'd', 'd', 'd', 'd', 'l', 'd', 'r', 'r', 'r', 'u', 'u']
# player2Moves = ['l', 'l', 'l', 'u', 'u', 'l', 'u', 'u', 'u', 'r', 'r', 'u', 'l', 'l', 'l', 'l', 'u', 'r']
# output: “Draw” … (because both eliminated on same turn)

 

# input:
# player1Moves = ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'r', 'r', 'r', 'r', 'r', 'u', 'u', 'u', 'u', 'u']
# player2Moves = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'l', 'l', 'l', 'l', 'l', 'd', 'd', 'd', 'd', 'd']
# output: “Draw” … (because both are alive at the end)

 

# input:
# player1Moves = ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'r', 'r', 'r', 'r', 'r', 'u', 'u', 'u', 'u', 'u']
# player2Moves = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'l', 'l', 'l', 'l', 'l', 'd', 'd', 'd', 'r', 'd']
# output: “Draw” … (because both land on the same space on same turn)

 

# input:
# player1Moves = ['d', 'd', 'd', 'd', 'u', 'u', 'r', 'd', 'd', 'd', 'd', 'l', 'd', 'r', 'r', 'r', 'u', 'u']
# player2Moves = ['l', 'l', 'l', 'l', 'r', 'l', 'u', 'u', 'u', 'r', 'r', 'u', 'l', 'l', 'l', 'l', 'u', 'r']
# output: “Draw” … (because both are eliminated separately, but both on the 5th round)

 

# input:
# player1Moves = ['r', 'd', 'd', 'r', 'r', 'r', 'd', 'r', 'r', 'd', 'd', 'd', 'l', 'd', 'd', 'd', 'd', 'r']
# player2Moves = ['u', 'l', 'l', 'u', 'l', 'l', 'u', 'l', 'l', 'd', 'd', 'l', 'l', 'u', 'u', 'r', 'u', 'l']
# output: “Player 2 wins”

 

# input:
# player1Moves = ['r', 'd', 'd', 'r', 'r', 'r', 'd', 'r', 'r', 'd', 'd', 'd', 'r', 'u', 'u', 'u', 'd', 'r']
# player2Moves = ['u', 'l', 'l', 'u', 'l', 'l', 'u', 'u', 'u', 'u', 'u', 'l', 'l', 'u', 'u', 'r', 'u', 'l']
# output: “Player 1 wins”

 

# input
# player1Moves = ['r', 'd', 'r', 'r', 'u', 'r', 'u', 'u', 'u', 'd', 'd', 'd', 'r', 'u', 'u', 'u', 'd', 'r']
# player2Moves = ['u', 'l', 'l', 'u', 'l', 'l', 'u', 'l', 'l', 'd', 'd', 'l', 'l', 'u', 'u', 'r', 'u', 'l']
# output: “Player 2 wins” … (because player 1 goes out of bounds)


# 2 players 
# 0,0 
# 9,9

# if the player is out of bounds losses
# if the player step on visited path if losses
# if both lose at the same time its a draw




def game(player1Moves: list[str], player2Moves: list[str]) -> None:
  n = 10
  player1 = (0, 0)
  player2 = (9, 9)
  board = [[''] * 10 for i in range(n)]
  print(board)
  
  for m in range(len(player1Moves)):  
    player1 = move(board, player1Moves[m], player1)
    if player1 is None: 
      print("player1 lose")
      return
      
    player2 = move(board, player2Moves[m], player2)
    if player2 is None: 
      print("player2 lose")
      return
      
    if player1 == player2: 
      print("its a draw")
      return

def move(board: list[list[int]], move: str, player: tuple[int, int]) -> tuple[int, int] | None:
  # print(player)
  (i, j) = player
  match move: 
    case 'r':
      i += 1
    case 'l': 
      i -= 1
    case 'd':
      j +=1
    case 'u':
      j -= 1
  
  # off the board
  if i >= len(board) and i < 0 and j >= len(board) and j < 0: 
    return None
  
  # collision
  if board[i][j] == 'v': 
    return None
  else: 
    board[i][j] = 'v'
  
  return (i, j)
  

# input:
player1Moves = ['r', 'd', 'd', 'r', 'r', 'r', 'l', 'l', 'l', 'd', 'd', 'd', 'l', 'd', 'd', 'd', 'd', 'r']
player2Moves = ['u', 'l', 'l', 'u', 'l', 'l', 'u', 'l', 'l', 'd', 'd', 'l', 'l', 'u', 'u', 'r', 'u', 'l']
# output: “Player 2 wins” … (because player 1 runs into their own path)

game(player1Moves, player2Moves)

# input:
# player1Moves = ['d', 'd', 'r', 'r', 'r', 'u', 'r', 'd', 'd', 'd', 'd', 'l', 'd', 'r', 'r', 'r', 'u', 'u']
# player2Moves = ['l', 'l', 'l', 'u', 'u', 'l', 'u', 'u', 'u', 'r', 'r', 'u', 'l', 'l', 'l', 'l', 'u', 'r']
# output: “Draw” … (because both eliminated on same turn)

 

# input:
# player1Moves = ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'r', 'r', 'r', 'r', 'r', 'u', 'u', 'u', 'u', 'u']
# player2Moves = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'l', 'l', 'l', 'l', 'l', 'd', 'd', 'd', 'd', 'd']
# output: “Draw” … (because both are alive at the end)

 

# input:
# player1Moves = ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'r', 'r', 'r', 'r', 'r', 'u', 'u', 'u', 'u', 'u']
# player2Moves = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'l', 'l', 'l', 'l', 'l', 'd', 'd', 'd', 'r', 'd']
# output: “Draw” … (because both land on the same space on same turn)







