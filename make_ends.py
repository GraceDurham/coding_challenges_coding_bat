

""" Given an array of ints, return a new array length 2 containing 
    the first and last elements from the original array.  The 
    original array will be length 1 or more."""


def make_ends(nums):

    	
	return[nums[0], nums[-1]]



print(make_ends([1,2,3]))
print(make_ends([1,2,3,4]))
print(make_ends([7,4,6,2]))
print(make_ends([1,2,2,2,2,2,2,3]))
print(make_ends([7,4]))
print(make_ends([7]))
print(make_ends([5,2,9]))
print(make_ends([2,3,4,1]))