from collections import Counter

def process(filename):
	# points = {}
	all_points = []

	f = open(filename)

	for line in f:

		tokens = line.strip().split(' -> ')
		start = tuple([ int(n) for n in tokens[0].split(',') ])
		end = tuple([ int(n) for n in tokens[1].split(',') ])

		line_points = set([start, end])
		print(f"start {start} end {end}")

		if start[0] == end[0]:

			x = start[0]
			current_y = min([start[1], end[1]]) + 1
			end_y = max([start[1], end[1]])

			while current_y != end_y:
				line_points.add((x, current_y))
				current_y += 1


		elif start[1] == end[1]:

			y = start[1]
			current_x = min([start[0], end[0]]) + 1
			end_x = max([start[0], end[0]])

			while current_x != end_x:
				line_points.add((current_x, y))
				current_x += 1

		else:
			line_points = get_points(start, end)

		all_points.extend(line_points)

		
		print(f"line points {line_points}")


	counts = Counter(all_points)

	print(len([k for k in counts if counts[k] > 1]))


def calc_slope(p1, p2):
	return int((p2[1]-p1[1]) / (p2[0]-p1[0]))

def calc_intercept(a, m):
	return int(a[1] - m*a[0])


def get_points(p1, p2):

	m = calc_slope(p1, p2)

	b = calc_intercept(p1, m)
	
	points = set()

	current_x = min([p1[0], p2[0]])
	end_x = max([p1[0], p2[0]])

	while current_x != end_x+1:
		current_y = m*current_x + b
		points.add((current_x, current_y))
		current_x += 1

	return points









if __name__ == "__main__":
	process("input.txt")