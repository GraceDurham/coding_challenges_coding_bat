


# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.


def not_string(str):

	new_str = " "
	if str.startswith("not"):
		return str
	new_str = "not " + str
	return new_str


print(not_string("candy"))
print(not_string("x"))
print(not_string("not bad"))


def not_strings(str):

	# str[:3] goes from the start of the string up to but not
	# including index 3

	if len(str) >= 3 and str[:3] == "not":
		return str 

	return "not " + str 


print(not_strings("candy"))
print(not_strings("x"))
print(not_strings("not bad"))	