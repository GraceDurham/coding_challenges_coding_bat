

# Return the number of times that the string
# "hi" appears anywhere in the given string.


def count_hi(str):

	count = 0

	for i in range(len(str)-1):
		if str[i] == "h" and str[i+1] == "i":
			count = count + 1
		count = count
	return count

print(count_hi("abc hi ho"))
print(count_hi("ABChi hi"))
print(count_hi("hihi"))
print(count_hi("hi hi hihi hi"))


def count_hi(str):
	
	count = 0

	## Loop to length-1 and access index i and i+1
	## in the loop.

	for i in range(len(str)-1):
		if str[i:i+2] == "hi":
			count = count + 1
	return count

print(count_hi("abc hi ho"))
print(count_hi("ABChi hi"))
print(count_hi("hihi"))
print(count_hi("hi hi hihi hi"))











