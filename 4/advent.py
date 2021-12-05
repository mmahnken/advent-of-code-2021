def process(filename):
	f = open(filename)
	nums = next(f).strip().split(',')
	nums = [int(num) for num in nums]
	boards = f.read().split('\n\n')
	formatted_boards = []

	for b in boards:
		fixed_board = []
		b = b.strip().split('\n')
		for line in b:
			line = [int(num) for num in line.split()]
			line = [BoardNumber(num) for num in line]
			fixed_board.append(line)

		b = BingoBoard(fixed_board)
		formatted_boards.append(b)
	return nums, formatted_boards

class BoardNumber:
	def __init__(self, data):
		self.data = data
		self.state = 'empty'

	def mark_num(self):
		self.state = 'covered'

	def covered(self):
		return self.state == 'covered'



class BingoBoard:
	def __init__(self, board):
		self.board = board
		self.bingo = False

	def pprint(self):
		for line in self.board:
			for num in line:
				print(f"{num.data:2} ", end="")
			print()
		print()

	def handle_num(self, num):
		# import pdb; pdb.set_trace()
		for line in self.board:
			for boardnum in line:
				if boardnum.data == num:
					boardnum.mark_num()

	def has_bingo(self):
		if self.bingo:
			return True
		
		# check horizontal win
		for line in self.board:
			if [n.covered() for n in line] == [True for n in line]:
				self.bingo = True
				return True


		# check vertical win
		for i in range(len(self.board)):
			if [line[i].covered() for line in self.board] == [True for n in self.board[0]]:
				self.bingo = True
				return True

		return False

	def calculate_final_score(self, final_num_called):
		sum_unmarked = 0
		for line in self.board:
			for boardnum in line:
				if not boardnum.covered():
					sum_unmarked += boardnum.data

		return sum_unmarked * final_num_called
			

def place_num(num, boards):
	for i, board in enumerate(boards):
		if board.has_bingo():
			continue
		board.handle_num(num)
		if board.has_bingo():
			print("BINGO", i)
			print(board.calculate_final_score(num))
			


if __name__ == "__main__":
	nums, boards = process("input.txt")
	for num in nums:
		print('placing', num)
		place_num(num, boards)






