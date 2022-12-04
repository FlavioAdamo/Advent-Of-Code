MOVES = {
   "A Y": 8,
   "A X": 4,
   "A Z": 3,
   "B Y": 5,
   "B X": 1,
   "B Z": 9, 
   "C Y": 2,
   "C X": 7,
   "C Z": 6,
}


def translate_move(move):
   LOSE = {"A": "Z", "B": "X", "C": "Y"}
   WIN = {"A": "Y", "B": "Z", "C": "X"}
   DRAW = {"A": "X", "B": "Y", "C": "Z"}

   if move[2] == 'Y':
      move = move[:-1] + DRAW[move[0]]
   elif move[2] == 'X':
      move = move[:-1] + LOSE[move[0]]
   elif move[2] == 'Z':
      move = move[:-1] + WIN[move[0]]
   return move
      

with open('input.txt', 'r') as input:
   moves = input.read().strip().split('\n')
   problem1 = [MOVES[move]for move in moves]
   problem2 = [MOVES[translate_move(move)]for move in moves]
   print(sum(problem1), sum(problem2))

