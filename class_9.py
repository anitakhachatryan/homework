my_tuple = "bmw", "mercedes", "audi", 15, False

text = ""
for i in my_tuple:
	text += str(i)
print(text)


tuple_2 = 5, 10, 15, 5, 3 # homework - count and sum all duplicates

my_list = ["4", "0", "1", "10", "2"]

a = 0
for i in my_list:
	if i.isdigit():
		if int(i) > 3:
			a += int(i)
print(a)


def is_even(list_1: list):
	even_sum = 0
	for i in list_1:
		if i % 2 == 0:
			even_sum += i
	return even_sum


list_2 = [10, 5, 3, 8, 1, 7, 6]

print(is_even(list_2))

