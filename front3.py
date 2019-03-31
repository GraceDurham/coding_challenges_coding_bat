

# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. 
# Return a new string which is 3 copies of the front. 


def front3(str):

	if len(str) < 3:
		return str * 3
	return str[:3] * 3


print(front3("Java"))
print(front3("Chocolate"))
print(front3("abc"))


def front3_coding_bat_solution(str):

	# Figure out the end of the front
	front_end = 3 
	if len(str) < front_end:
		front_end = len(str)
	front = str[:front_end]
	return front + front + front 

	# Could omit the if logic, and write simply front = str[:3]
  	# since the slice is silent about out-of-bounds conditions.


print(front3_coding_bat_solution("Java"))
print(front3_coding_bat_solution("Chocolate"))
print(front3_coding_bat_solution("abc"))





def front3_(str):

	return str[:3] * 3

print(front3_("Java"))
print(front3_("Chocolate"))
print(front3_("abc"))