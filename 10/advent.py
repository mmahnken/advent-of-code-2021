char_lookup = {'{': '}', '[':']', '<':'>', '(':')'}


class Line:
	def __init__(self, characters):
		self.characters = characters

	def is_corrupted(self):
		stack = []

		for c in self.characters:
			if c in '{[(<':
				stack.append(c)
			elif c in '}])>':
				opener = stack.pop()
				if char_lookup[opener] != c:
					self.corrupt_char = c
					self.corrupted = True
					# print(f'corrupt char is {c}')
					return True


	def is_incomplete(self):
		stack = []

		for c in self.characters:
			# print(f"stack {''.join(stack)} char {c}")
			# import pdb; pdb.set_trace()
			if c in '{[(<':
				stack.append(c)
			elif c in '}])>':
				opener = stack.pop()
				if char_lookup[opener] == c:
					continue
				else: 
					self.corrupted = True
					return False


		# import pdb; pdb.set_trace()
		if stack:
			self.incomplete = True
			self.completion_string = ''.join([char_lookup[char] for char in stack[::-1]])
			return True
		else:
			return False
			# self.incomplete = True


def process(filename):
	f = open(filename)
	lines = []

	for line in f:
		l = Line(line.strip())
		lines.append(l)
	
	return lines

def find_corrupted_lines(lines):
	corrupt_chars = []

	for l in lines:
		if l.is_corrupted():
			corrupt_chars.append(l.corrupt_char)
	return corrupt_chars


def tally_corrupt_chars(chars):
	total = 0
	for char in chars:
		if char == "}":
			total += 1197
		elif char == ")":
			total += 3
		elif char == ">":
			total += 25137
		elif char == "]":
			total += 57

	print(total)

def find_incomplete_lines(lines):
	completion_strings = []

	for l in lines:
		if l.is_incomplete():
			print(l.characters, "INCOMPLETE", "completion", l.completion_string)
			completion_strings.append(l.completion_string)

			
	return completion_strings

def tally_completion_strings(strings):

	point_table = { ')': 1,
					']': 2,
					'}': 3,
					'>': 4,
	              }
	string_totals = []
	for s in strings:
		string_total = 0
		for char in s:
			string_total *= 5 
			string_total += point_table[char]
		string_totals.append(string_total)
	
	string_totals.sort()

	print(string_totals[len(string_totals)//2])


if __name__ == "__main__":
	lines = process("input.txt")

	# corruptions = find_corrupted_lines(lines)
	# tally_corrupt_chars(corruptions)

	incompletes = find_incomplete_lines(lines)
	tally_completion_strings(incompletes)