class Point:

	
	def __init__(self, data):
		self.data = data


	def set_neighbors(self, i, row, before_row=None, after_row=None):

		self.i = i
		self.before_row = before_row
		self.after_row = after_row
		
		# not last, has right
		if i != len(row)-1:
			self.right = row[i+1]
		else:
			self.right = None

		# not first, has left
		if i != 0:
			self.left = row[i-1]
		else: self.left = None


		# not the first row
		if before_row:
			self.above = before_row[i]
		else: self.above = None


		# not the last row
		if after_row:
			self.below = after_row[i]
		else: self.below = None

		self.adjacent = [p for p in [self.below, self.above, self.right, self.left] if p != None]


	def is_low_point(self):


		points = [self.below, self.above, self.right, self.left]

		points = [p.data for p in points if p != None]

		

		less_than = True
		for p in points:
			if self.data >= p:
				less_than = False

		return less_than

	def find_basin(self):
		


		to_visit = set(self.adjacent)
		seen = set()
		num_locations = 0

		while to_visit:
			# import pdb; pdb.set_trace()
			current = to_visit.pop()
			seen.add(current)

			if current.data != 9:
				num_locations += 1
				for p in current.adjacent:
					if p not in seen:
						to_visit.add(p)


		return num_locations



	def get_risk_level(self):
		return self.data + 1

	def __repr__(self):
		return f"<Point data={self.data}>"



class Graph:

	def __init__(self):
		self.nodes = []


def process(filename):
	f = open(filename)

	rows = []

	for line in f:

		nums = line.strip()
		nums = [int(n) for n in nums]
		rows.append(nums)


	return rows


def make_points(array2d):

	array2d_points = []

	for i, row in enumerate(array2d):
		new_row = []

		for j, point in enumerate(row):
	
			p = Point(point)

			new_row.append(p)

		array2d_points.append(new_row)

	return array2d_points


def set_neighbors(array2d_points):

	g = Graph()

	for i, row in enumerate(array2d_points):
		for j, point in enumerate(row):
			# import pdb; pdb.set_trace()
			if i == 0:
				point.set_neighbors(j, row, after_row=array2d_points[i+1])


			elif i == len(array2d_points)-1:
				point.set_neighbors(j, row, before_row=array2d_points[i-1])

			else:
				point.set_neighbors(j, row, before_row=array2d_points[i-1], after_row=array2d_points[i+1])


			# print(f"ADDED POINT {p}")
			g.nodes.append(point)


	return g

def count_lows(g):

	overall_risk_level = 0
	count = 0
	lows = []
	for n in g.nodes:
		if n.is_low_point():
			# import pdb; pdb.set_trace()
			# count += 1
			lows.append(n)
			overall_risk_level += n.get_risk_level()

	print(len(lows))
	print(f"risk level {overall_risk_level}")
	return lows


def find_basin_sizes(lows):

	basins = []

	for l in lows:
		size = l.find_basin()

		basins.append(size)


	basins.sort()

	print(basins[-1] * basins[-2] * basins[-3])


if __name__ == "__main__":
	nums = process("input.txt")
	array2d_points = make_points(nums)
	g = set_neighbors(array2d_points)
	# g = make_graph(nums)
	lows = count_lows(g)
	find_basin_sizes(lows)
