

def double_char(string):

	''' Given a string, return a string where
	for for every char in the original, there
	are two chars.'''

	new_str = ""

	for str in string:
		double = str * 2
		new_str = new_str + double

	return new_str

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))