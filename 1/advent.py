def process(filename):
	return [int(line.strip()) for line in open(filename)]


def count_increases(nums):
	count = 0
	previous = nums[0]

	for num in nums[1:]:
		if num > previous:
			count += 1
		previous = num
	return count

def count_window_increases(nums):
	count = 0
	previous = sum(nums[0:3])

	for i in range(1, len(nums)-2):
		current = sum(nums[i:i+3])

		if current > previous:
			count += 1
		
		previous = current

	return count

if __name__ == "__main__":
	nums = process("input.txt")
	# print(count_increases(nums))
	print(count_window_increases(nums))