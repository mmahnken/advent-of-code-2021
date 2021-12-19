

class Octopus:
	def __init__(self, energy):
		self.energy = energy
		self.adjacent = []
		self.frozen = False

	
	def flash(self):
		if not self.frozen and self.energy > 9:
			self.energy = 0
			self.frozen = True

			for o in self.adjacent:
				o.increment()

			return True
		else:
			return False

	def increment(self):
		self.energy = self.energy + 1



class Graph:

	def __init__(self):
		self.nodes = []
		self.num_flashes = 0



	def step(self):
		for row in self.nodes:
			for octo in row:
				octo.increment()


		while True:
			result, num_flashes = self.flash_all()
			if not result:
				break



		self.reset()
		self.pprint()
		print()
		print()

	def take_n_steps(self, n):
		for i in range(n):
			self.step()

		print(f"Stepping complete, flash count {self.num_flashes}")

	def step_part2(self):
		for row in self.nodes:
			for octo in row:
				octo.increment()

		total_step_flashes = 0
		while True:
			result, num_flashes = self.flash_all()
			total_step_flashes += num_flashes
			if not result:
				break

		self.reset()
		self.pprint()
		print()
		print()

		return total_step_flashes

	def step_until_simultaneous_flash(self):
		step_count = 1	
		num_octos = len(self.nodes) * len(self.nodes[0])

		while True:
			num_flashes = self.step_part2()

			if num_flashes == num_octos:
				print(f'step number {step_count}')
				return
			step_count += 1



		num_octos = len(self.nodes) * len(self.nodes[0])
		if num_flashes == num_octos:
				return

	def reset(self):
		for row in self.nodes:
			for octo in row:
				if octo.frozen == True:
					octo.energy = 0
					octo.frozen = False

	def flash_all(self):
		step_flash_count = 0
		flash_happened = False
		
		for row in self.nodes:
			for octo in row:
				result = octo.flash()
				if result == True: 
					flash_happened = True
					step_flash_count += 1

		self.num_flashes += step_flash_count

		return flash_happened, step_flash_count


	def set_neighbors(self):

		for i, row in enumerate(self.nodes):
			for j, octo in enumerate(row):
				print(f'i {i} j {j}')

				row_above = (i != 0)
				row_below = (i != len(row)-1)
				space_to_right = (j != len(self.nodes)-1)
				space_to_left = (j != 0)
				# import pdb; pdb.set_trace()


				if row_below:
					octo.adjacent.append(self.nodes[i+1][j])
					

				if row_above:
					octo.adjacent.append(self.nodes[i-1][j])
					

				if space_to_left:
					octo.adjacent.append(self.nodes[i][j-1])
					

				if space_to_right:
					octo.adjacent.append(self.nodes[i][j+1])

				if row_above and space_to_left:
					octo.adjacent.append(self.nodes[i-1][j-1])


				if row_above and space_to_right:
					octo.adjacent.append(self.nodes[i-1][j+1])


				if row_below and space_to_left:
					octo.adjacent.append(self.nodes[i+1][j-1])


				if row_below and space_to_right:
					octo.adjacent.append(self.nodes[i+1][j+1])


	def pprint(self):
		for row in self.nodes:
			for octo in row:
				print(octo.energy, end="")
			print()



def process(filename):
	f = open(filename)
	g = Graph()

	for line in f:
		nums = [int(n) for n in line.strip()]
		# import pdb; pdb.set_trace()
		row = []
		for num in nums:
			o = Octopus(num)
			row.append(o)
		g.nodes.append(row)


	g.set_neighbors()

	return g



if __name__ == "__main__":
	g = process("input.txt")
	# g.take_n_steps(100)
	g.step_until_simultaneous_flash()