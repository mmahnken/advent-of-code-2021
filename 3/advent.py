from collections import Counter
from copy import copy

def process(filename):
	
	counts = {}
	for line in open(filename):
		line = line.strip()

		for idx, char in enumerate(line):
			if not counts.get(idx):
				counts[idx] = []

			counts[idx].append(char)

	return counts

def organize_bits(counts):

	gamma = []
	epsilon = []


	for k in counts:
		counter = Counter(counts[k])

		if counter['0'] > counter['1']:
			gamma.append('0')
			epsilon.append('1')
		else:
			gamma.append('1')
			epsilon.append('0')


	gamma = int("".join(gamma), 2)
	epsilon = int("".join(epsilon), 2)

	print(gamma*epsilon)



def determine_next_char(nums, idx, diagnostic):

	counter = Counter([num[idx] for num in nums])
	# import pdb; pdb.set_trace()

	if counter['0'] > counter['1']:
		if diagnostic == "o2":
			return "0"
		if diagnostic == "co2":
			return "1"
	elif counter['1'] > counter['0']:
		if diagnostic == "o2":
			return "1"
		if diagnostic == "co2":
			return "0"
	elif counter['1'] == counter['0']:
		if diagnostic == "o2":
			return "1"
		if diagnostic == "co2":
			return "0"

def process2(filename):
	nums = set()

	for num in open(filename):
		num = num.strip()
		nums.add(num)
	return nums

def find_num(nums, diagnostic):
	
	char = determine_next_char(nums, 0, diagnostic=diagnostic)

	for idx in range(len(nums)):
		print(f"nums {nums}")
		print(f'matching idx {idx} for bit {char}')
		nums2 = copy(nums)
		for num in nums2:
			if num[idx] != char:
				nums.remove(num)

		if len(nums) == 1:
			return int(nums.pop(), 2)

		char = determine_next_char(nums, idx+1, diagnostic=diagnostic)


if __name__ == "__main__":
	# counts = process("test.txt")
	nums = process2("input.txt")

	o2 = find_num(copy(nums), 'o2')
	co2 = find_num(copy(nums), 'co2')

	print(o2*co2)

	


