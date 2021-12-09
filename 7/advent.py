def process(filename):
	f = open(filename)
	nums = f.read().strip().split(',')
	nums = [int(n) for n in nums]
	return nums


def get_fuel_cost(num_steps):

	total = 0
	adder = 0
	for i in range(num_steps+1):

		total += adder

		adder += 1

	return total


def calc_part1(nums):
	
	best_seen = float("inf")
	best_num = None


	for num in nums:
		print(f"trying {num} ")
		fuel = 0
		for num2 in nums:
			x = abs(num2 - num)
			print(f'aligning {num2} to {num} costs {x}')
			fuel += x

		print(f"fuel used {fuel}")

		if fuel < best_seen:
			best_seen = fuel
			best_num = num

	print(best_num, best_seen)



def calc_part2(nums):
	
	smallest = min(nums)
	largest = max(nums)
	# print(f"{smallest} {largest}")

	best_seen = float("inf")
	best_num = None

	fuel_costs = {}

	for num in range(smallest, largest+1):
		# print((num/(largest-smallest)*100))
		# print(num)
		
		fuel = 0
		for num2 in nums:
			x = abs(num2 - num)
			
			if x not in fuel_costs:
				cost = get_fuel_cost(x)
			else:
				cost = fuel_costs[x]

			fuel += cost

		

		if fuel < best_seen:
			best_seen = fuel
			best_num = num

	print(best_num, best_seen)




if __name__ == "__main__":
	nums = process("input.txt")
	calc_part2(nums)