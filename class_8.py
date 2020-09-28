from random import randint

# def happy_birthday():
# 	a = input("Provide your name: ")
# 	print("Happy Birthday,", a)


# # happy_birthday(input("Please provide your name: "))
# happy_birthday()

# # 2nd option 
# def happy_birthday(a):
# 	b = f"happy Bday, {a}"
# 	return b

# greeting = happy_birthday("Anita")
# print(greeting)

# v = "hello"
# def sum_1(a,b,c = 0):
# 	global v 
# 	v = a + b + c
	#print(v)

# sum_1(2,1)
# sum_1(2,1,4)
#print(v)


# print(randint.__doc__)
# help(randint)

# def my_function(a: str, b: str) -> str:
# 	pass
# print(my_function.__annotations__)

#factorial task with function

# def factorial_func(c):
# 	factorial = 1
# 	for i in range(1, c + 1):
# 		factorial *= i
		
# 	return factorial

# print(factorial_func(5))


# def factorial_(a):
# 	if a <= 0:
# 		b = 1
# 	else:
# 		b = a * factorial_(a - 1)
# 		return b

# print(factorial_(5))

# def smth(a,c):

# 	if c == 0:
# 		print("zero division")
# 		return
# 	value = int(a/c)
# 	return value



# def volume(l, d, h = 1):
# 	vol = l * d * h
# 	return vol

# print(volume(2,4))
# print(volume(2,4,5))

# def vol_(a,b,c):
# 	vol = a * b * c
# 	print(vol)

# a_input = int(input("num"))
# b_input = int(input("num"))
# c_input = int(input("num"))

# vol_(a_input, b_input, c_input)

check = "yes"
user_score = 0
computer_score = 0
round_ = 0
while check == "yes":

	user_choice = int(input("tell me, 1 for scissor, 2 for paper, 3 for rock: "))
	computer_choice = randint(1,3)

	if (user_choice == 1 and computer_choice == 2) or\
	 (user_choice == 2 and computer_choice == 3) or\
	  (user_choice == 3 and computer_choice == 1):
		user_score += 1
	elif user_choice == computer_choice:
		print("Tie")
	else:
		computer_score += 1

	round_ += 1
	check = ""
	while check != "no" and check != "yes":
		check = input("Do you want to play again?type yes for yes, no for no ")

print(f"Have you enjoyed the game?\n Your score is {user_score}\n computer score is {computer_score}\n rounds played {round_}")