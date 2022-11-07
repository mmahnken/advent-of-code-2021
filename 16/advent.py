from copy import copy

def process(filename):
	risk_levels = []
	f = open(filename)
	for row in f:
		current = row.strip()
		current = [int(n) for n in current]
		risk_levels.append(current)

	return risk_levels

def outer(risk_levels):
	memo = {}
	width = len(risk_levels[0])
	height = len(risk_levels)
	

	def get_lowest_risk(risk_levels, x, y):
		current_risk = risk_levels[y][x]
		

		if x == width-1 and y == height-1: # on final square
			return current_risk
		else:
			risk_right = None
			risk_down = None

			# go right if you can
			if x < width-1: 
				next_point = f"{x+1}.{y}"

				path2_memoized = memo.get(next_point)
				if path2_memoized:
					path2_right_memoized = path2_memoized.get('right')
					if path2_right_memoized:
						risk_right = path2_right_memoized
					else:
						risk_right = current_risk + get_lowest_risk(risk_levels, x+1, y)
						memo[next_point]['right'] = risk_right
				else:
					risk_right = current_risk + get_lowest_risk(risk_levels, x+1, y)
					memo[next_point] = {'right': risk_right, 'down': None}



			# go down if you can
			if y < height-1:
				next_point = f"{x}.{y+1}"

				path2_memoized = memo.get(next_point)
				if path2_memoized:
					path2_down_memoized = path2_memoized.get('down')
					if path2_down_memoized:
						risk_down = path2_down_memoized
					else:
						risk_down = current_risk + get_lowest_risk(risk_levels, x, y+1)
						memo[next_point]['down'] = risk_down
				else:
					risk_down = current_risk + get_lowest_risk(risk_levels, x, y+1)
					memo[next_point] = {'right': None, 'down': risk_down}


			if not risk_right:
				return risk_down
			elif not risk_down:
				return risk_right
			else:
				choice = min([risk_down, risk_right])
				return choice

				
	answer = get_lowest_risk(risk_levels, 0, 0) - risk_levels[0][0]
	return answer




if __name__ == "__main__":
	risk_levels = process("input.txt")
	print(outer(risk_levels))
