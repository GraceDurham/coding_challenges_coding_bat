


#  Given a string,
#  return a new string where the first and last chars have been exchanged.



def front_back(str):

	if len(str) > 1:
		front = str[0]
		back = str[-1]
		front_back = back + str[1:-1] + str[0]
		return front_back

	else:
		return str

print(front_back("code"))
print(front_back("a"))
print(front_back("ab"))



def front_back_code_solution(str):

	if len(str) <= 1:
		return str

	mid = str[1:len(str) -1]  # can be written as str[1:-1]

	# last + middle + first

	return str[len(str)-1] + mid + str[0]


print(front_back_code_solution("code"))
print(front_back_code_solution("a"))
print(front_back_code_solution("ab"))















