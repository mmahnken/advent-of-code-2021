def process(filename):
	f = open(filename)

	points = []
	folds = []
	for line in f:
		if not line.startswith('fold along') and not line.startswith('\n'):
			x, y = line.strip().split(',')
			points.append((int(x), int(y)))

		elif not line.startswith('\n'):
			tokens = line.strip().split(' along ')
			fold = tokens[1]
			axis, value = fold.split('=')
			folds.append((axis, int(value)))

	return points, folds


def fold_paper(points, fold):
	# print('FOLDING', fold)
	axis, val = fold
	new_points = set()
	if axis == 'y':
		for p in points:
			# is it below the fold
			if p[1] > val:
				# print('folding up', p)
				distance_from_line = p[1]-val
				y = p[1] - distance_from_line*2
			else:
				y = p[1]

			new_points.add((p[0], y))
	elif axis == 'x':
		for p in points:
			# is it below the fold
			if p[0] > val:
				# print('folding up', p)
				distance_from_line = p[0]-val
				x = p[0] - distance_from_line*2
			else:
				x = p[0]

			
			new_points.add((x, p[1]))
	# pprint(new_points)
	return new_points


def complete_all_folds(points, folds):
	for fold in folds:
		points = fold_paper(points, fold)
	return points


def pprint(points):
	max_x = max([p[0] for p in points])
	max_y = max([p[1] for p in points])

	for y in range(max_y+1):
		for x in range(max_x+1):
			if (x, y) in points:
				print('#', end="")
			else:
				print('.', end="")
		print()

	print()
	print()



if __name__ == "__main__":
	points, folds = process("input.txt")
	# pprint(points)
	# points = fold_paper(points, folds[0])
	# points = fold_paper(points, folds[1])

	points = complete_all_folds(points, folds)
