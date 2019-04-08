


# Given an array of ints length 3, 
# return an array with the elements "rotated left"
# so {1,2,3} yields {2,3,1} without using a for loop and only using indexes


def rotate_left3(nums):
	return [nums[1], nums[len(nums) -1], nums[0]]


print(rotate_left3([1,2,3])==[2,3,1])
print(rotate_left3([5,11,9])==[11,9,5])
print(rotate_left3([7,0,0])==[0,0,7])