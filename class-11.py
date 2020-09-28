# try/except

# user_answer = input("tell smth: ")

# try:
# 	my_number = int(user_answer)
# 	value = 10 / my_number
# except ValueError:
# 	print("wrong value, its not a digit")
# 	my_number = 0
# except ZeroDivisionError:
# 	print("the  number could not be 0")
# 	value = 10


# my_number += 5

# try:	
# 	print(value)
# except NameError:
# 	print("you didnt give a number thats why you could not see the VALUE")

# Dictionaries

# my_dict = {"key1": [1, 2, 3], "key2": 5}


# a = my_dict["key1"]
# print(a[0])

# a_key = "key1"
# my_dict = {a_key:{1:"2","4":3}, (1,2): 5}


# a = my_dict[a_key][1]
# print(a)
# b = my_dict[(1,2)]
# print(b)
# b = my_dict.get((1,2))
# print(b)

# a_key = "key1"
# my_dict = {a_key:"hello", (1,2): 5}
# #my_dict = {a_key:"hello", None: 5}

# my_dict[5] = "Armenia"
# print(my_dict)
# my_dict[5] = "Ani"
# print(my_dict)

# for key in my_dict:
# 	print("key", key, "value", my_dict[key])


dict_1 = {"key1":1, "key2":2}
dict_2 = {"key1":10, "key3":3, "key4":4,}
#dict_3 = {}

for key in dict_2:
	dict_1[key] = dict_2[key]

# print(dict_2)
# print(dict_1)
# for i in dict_1:
# 	dict_3[i] = dict_1[i]

# for j in dict_2:
# 	dict_3[j] = dict_2[j]

# print(dict_3)
dict_2["key4"] = dict_2.pop("key4")
print(dict_2)
# list_dict = [dict_1, dict_2, dict_3]
#dict_3 = {}

dict_2["key1"] = 50
# dict_2.popitem()
# print(dict_2)

dict_2.clear()

# del dict_2

print(dict_2)

dict_1.update(dict_2)
print(dict_1)