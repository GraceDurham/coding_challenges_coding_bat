

# Without using any loops and just using indexes of a list 
# Given an array of ints length of 3
# Figure out which is larger, the first or last element in the array
# And set all the other elements to be that value.
# Return the changed array


def max_end3(nums):
	if nums[0] > nums[(len(nums)) -1 ]:
		first_big = nums[0]
		return [first_big, first_big, first_big]
	else:
		last_big = nums[len(nums)-1]
		return[last_big, last_big, last_big]


print(max_end3([1,2,3])==[3,3,3])
print(max_end3([11,5,9])==[11,11,11])
print(max_end3([2,11,3])==[3,3,3])


def max_end3_coding_bat_solution(nums):

	big = max(nums[0], nums[2])
	nums[0] = big
	nums[1] = big
	nums[2] = big
	return nums


print(max_end3_coding_bat_solution([1,2,3]) == [3,3,3])
print(max_end3_coding_bat_solution([11,5,9])==[11,11,11])
print(max_end3_coding_bat_solution([2,11,3])==[3,3,3])























