"""

0: 6
1: 2
2: 5
3: 5
4: 4
5: 5
6: 6
7: 3
8: 7
9: 6


org
---

4: 4
1: 2
7: 3
8: 7

2: 5
3: 5
5: 5

6: 6
0: 6
9: 6

"""

def process(filename):
	f = open(filename)

	easy_num_count = 0

	for line in f:
		# import pdb; pdb.set_trace()
		notes, digit = line.strip().split(' | ')
		
		notes = notes.split(' ')
		digit = digit.split(' ')

		lengths = [len(d) for d in digit]

		for l in lengths:
			if l in [2, 3, 4, 7]:
				easy_num_count += 1

	print(easy_num_count)

def process_part2(filename):
	f = open(filename)
	overall_sum = 0

	for line in f:
		# import pdb; pdb.set_trace()
		notes, digit = line.strip().split(' | ')
		
		notes = notes.split(' ')
		digit = digit.split(' ')

		nums = get_signal_mapping(notes, digit)
		

		nums = sort_and_switch(nums)

		# import pdb; pdb.set_trace()

		decoded_digit = ""
		for num in digit:
			num = "".join(sorted(num))
			# import pdb; pdb.set_trace()			
			decoded_digit = decoded_digit + str(nums[num])


		overall_sum += int(decoded_digit)
		print(f"SUCCESS {decoded_digit}")
		# return

	print(overall_sum)


def sort_and_switch(dictionary):

	result = {}
	for k in dictionary:
		new_key = "".join(sorted(dictionary[k]))
		result[new_key] = k

	return result




def get_signal_mapping(notes, digit):

	num_mapping = {k: None for k in range(10)}
	components = {k: None for k in 'abcdefg'}


	for note in notes:
		if len(note) == 2:
			# num is 1
			num_mapping[1] = note

		elif len(note) == 3:
			# num is 7
			num_mapping[7] = note

		elif len(note) == 4:
			# num is 4
			num_mapping[4] = note

		elif len(note) == 7:
			# num is 8
			num_mapping[8] = note

	components['a'] = (set(num_mapping[1]) ^ set(num_mapping[7])).pop()
	
	
	num_mapping[9] = find_nine(notes, num_mapping[4], num_mapping[1], num_mapping[8], components['a'])
	num_mapping[6] = find_six(notes, num_mapping[1], num_mapping[9])

	components['c'] = (set('abcdefg') ^ set(num_mapping[6])).pop()

	components['e'] = (set(num_mapping[8]) ^ set(num_mapping[9])).pop()
	num_mapping[0] = find_zero(notes, num_mapping[6], num_mapping[9])
	
	num_mapping[5] = find_five(notes, components['c'])
	num_mapping[2] = find_two(notes, components['e'], components['c'])
	# import pdb; pdb.set_trace()
	
	num_mapping[3] = find_three(notes, num_mapping[2], num_mapping[5])
	
	
	return num_mapping

def decode(str, component_mapping):
	
	new_str = ""
	for letter in str:
		replacement = component_mapping.get(letter)
		if replacement:
			new_str = new_str + replacement
		else:
			new_str = new_str + letter

	return new_str


def find_nine(notes, four, one, eight, a):
	bd = "".join(set(four) ^ set(one))
	all_but_ge = bd + a + one
	ge = "".join(set('abcdefg') ^ set(all_but_ge))
	cf = one

	# has bd, has cf, doesn't have BOTH eg, len is 6
	poss = [n for n in notes if (len(n) == 6)]
	poss = [n for n in poss if bd[0] in n and bd[1] in n]
	poss = [n for n in poss if cf[0] in n and cf[1] in n]
	poss = [n for n in poss if len(set(n) & set(ge)) == 1]
	
	if not len(poss) == 1:
		raise Exception("got more than one answer for 9")

	return poss.pop()


	

	


def find_six(notes, one, nine):
	poss = [n for n in notes if len(n) == 6 and n != nine]

	poss = [p for p in poss if len(set(one) & set(p)) != 2]

	if not len(poss) == 1:
		raise Exception("got more than one answer for 6")

	return poss.pop()
	

def find_zero(notes, six, nine):
	answer = [n for n in notes if len(n) == 6 and n not in [six, nine]]
	return answer.pop()


def find_two(notes, e, c):
	answer = [n for n in notes if len(n) == 5 and (e in n) and (c in n)]
	return answer.pop()


def find_three(notes, two, five):
	# import pdb; pdb.set_trace()
	answer = [n for n in notes if ((len(n) == 5) and (n != two) and (n != five))]
	return answer.pop()


def find_five(notes, c):
	answer = [n for n in notes if len(n) == 5 and c not in n]
	return answer.pop()


	# num components
	# a: diff between 1 & 7
	# b:
	# c: whatever 6 doesn't have
	# d:
	# e: diff between 8 & 9
	# f:
	# g:


	# num mapping
	# -------------
	# how to ID 0: X
	# how to ID 1: X
	# how to ID 2:
	# how to ID 3:
	# how to ID 4: X
	# how to ID 5:
	# how to ID 6: X
	# how to ID 7: X
	# how to ID 8: X
	# how to ID 9: X




if __name__ == "__main__":
	process_part2("input.txt")
	# pass
