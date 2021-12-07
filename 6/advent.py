from collections import Counter


STATES = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def process(filename):

	f = open(filename)

	nums = f.read().strip().split(',')
	nums = [int(n) for n in nums]

	return nums


# def get_ancestors(fish_start, num_days):

# 	days_left = num_days - fish_start

# 	full_cycles = days_left // 7

# 	fish_end = days_left % 7

# 	return 1 + full_cycles

def setup_log(nums):
	log = Counter(nums)

	for s in STATES:
		if s not in log:
			log[s] = 0

	return log

def pprint_fish(log):
	lineup = []
	for s in STATES:
		lineup.extend([s for i in range(log[s])])
	# print(lineup)

def count_fish(log):
	count = 0	
	for k in log:
		count += log[k]
	return count


def step_through_time(nums, days):

	log = setup_log(nums)

	for i in range(1, days+1):
		print(f"on day {i}")
		# pprint_fish(log)

		new_log = {}
		for state in STATES:
			if state == 0:
				# add new fish
				new_log[8] = log[0]

				# changes 0s to 6s
				new_log[6] = log[0]
			elif state == 6:
				# change current 6s to 5s
				new_log[state-1] = log[state]

				# keep renewed 6s
				current = new_log[6]
				to_add = log[7]
				new_log[6] = current + to_add

			elif state != 7:
				new_log[state-1] = log[state]

		log = new_log

	print(count_fish(log))




if __name__ == "__main__":
	nums = process("input.txt")
	step_through_time(nums, 256)
