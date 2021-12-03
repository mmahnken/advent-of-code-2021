def process(filename):

	horiz = 0
	depth = 0

	for line in open(filename):
		tokens = line.strip().split()

		direction = tokens[0]
		val = int(tokens[1])
		print(f"dir {direction} val {val}")

		if direction == "forward":
			horiz += val
		elif direction == "down":
			depth += val
		elif direction == "up":
			depth -= val

	print(horiz * depth)


def process_part2(filename):

	horiz = 0
	depth = 0
	aim = 0

	for line in open(filename):
		tokens = line.strip().split()

		direction = tokens[0]
		val = int(tokens[1])
		# print(f"dir {direction} val {val}")

		if direction == "forward":
			horiz += val
			depth += (aim * val)
		elif direction == "down":
			aim += val
		elif direction == "up":
			aim -= val

	print(horiz * depth)





if __name__ == "__main__":
	# process("test.txt")
	process_part2("input.txt")