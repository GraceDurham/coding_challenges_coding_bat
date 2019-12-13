

# Return the sum of the numbers in the array,
# returning 0 for an empty array.
# Except the number 13 is very unlucky,
# so it does not count and numbers that
# come immediately after a 13 also do not count.



def sum13(nums):

	sum = 0

	if len(nums) == 0:
		return 0

	for i in range(1, len(nums)):
		if nums[i] == 13 or nums[i-1] == 13:
			sum = sum
		else:
			sum = sum + nums[i]
	if nums[0] == 13:
		return sum
	else:
		return sum + nums[0]

print(sum13([1, 2, 2, 1]))
print(sum13([1,1]))
print(sum13([1,2,2,1,13]))
print(sum13([1, 2, 13, 2, 1, 13]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))
print(sum13([]))
print(sum13([13]))
print(sum13([13, 13]))
print(sum13([13, 0, 13]))
print(sum13([13, 1, 13]))
print(sum13([5, 7, 2]))
print(sum13([5, 13, 2]))
print(sum13([0]))
print(sum13([13, 0]))




