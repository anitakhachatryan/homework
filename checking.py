import random
from heapq import nlargest
#1
def dictionary():
	string = input("input: \n")

	length = len(string)
	my_dict = {}

	for i in range(length):
		x = random.randint(0,9)
		my_dict.update({string[i]:x})

	return my_dict

a = dictionary()
print(a)

#2
def duplicate(dict1):
	result = {}
	for key, value in dict1.items():
		if value not in result.values():
			result.update({key:value})
			
	return result

dict2 = {'a': 70, 'b':20, 'c':10, 'd':30, 'e':40, 'f':10}

test = duplicate(dict2)
print(test)

#3
def largest(dict3):
	three_largest = nlargest(3, dict3, key = dict3.get)
	return three_largest

largest_nums = largest(dict2)
print(largest_nums)
