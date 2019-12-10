


# Given an array length 1 or more of ints
# Return the difference between the largest
# and the smallest values in the array.




def big_diff(nums):
	""" Return the difference between the largest and smallest
	    values in the array """

	min_num = nums[0]
	max_num = nums[0]

	for num in nums:
		if num > max_num:
			max_num = num
		if num < min_num:
			min_num = num

	return max_num - min_num


print(big_diff([10, 3, 5, 6]))
print(big_diff([7, 2, 10, 9]))
print(big_diff([2, 10, 7, 2]))