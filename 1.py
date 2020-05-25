def find_all_numbers(user_string):
	numbers_array = ['0','1','2','3','4','5','6','7','8','9']
	counter = 0
	for x in user_string:
		if x in numbers_array:
			counter+=1
	return counter

user_string = input()
print(find_all_numbers(user_string))