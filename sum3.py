

# Given an array of integers length of 3, return the sum of all the elements with out a using loops and only indexes.


def sum3(nums):

	return(nums[0] + nums[1] + nums[len(nums) -1 ])


print(sum3([1,2,3]) == 6)
print(sum3([5,11,2]) == 18)
print(sum3([7,0,0]) == 7)
