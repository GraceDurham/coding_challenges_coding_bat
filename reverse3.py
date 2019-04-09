


# Given an array of ints length of 3, 
# Return a new array with the elements
# In reverse order,
# So {1,2,3} becomes {3,2,1}
# You can not use a for loop or while loop only with indexes 



def reverse3(nums):
	return [nums[len(nums)-1], nums[1], nums[0]]


print(reverse3([1,2,3]) == [3,2,1])
print(reverse3([5,11,9]) == [9,11,5])
print(reverse3([7,0,0]) == [0,0,7])