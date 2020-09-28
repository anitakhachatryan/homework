import random

# multiplication table
# for i in range(1, 11):
# 	print(f"this is for {i}")
# 	for j in range(1, 11):
# 		print(f"{i} * {j} = {i*j}")


#
# for i in range(1,7):
# 	print(i*"*")
# 	if i == 6:
# 		for j in range(5, 0, -1):
# 			print(j*"*")


# a = 7
# b = 5

# while a > b:
# 	print(f"{a} > {b}")
# 	a -= 1

# password = input("Your password\n")

# while len(password) < 8 :
# 	password = input("Your password\n")

# password2 = input("Please enter your password:\n")

# while len(password2) > 8:
# 	if password2.find('.') != -1:
# 		print("Hi!")
# 		break
# 	else:
# 		password2 = input("Please enter your password:\n")


# while True:
# 	password = input("your pass:\n")

# 	if len(password) > 8:
# 		if "." in password:
# 			break
# print("ok!")



#import random

# num_guess = 5
# bonus = 0

# a = random.randint(1,3)
# b = int(input("Please input your guess: "))
# while num_guess != 0:
# 	if a != b:
# 		b = int(input("Try again! "))
# 		a = random.randint(1,3)
# 		num_guess -= 1
		
# 	else: 
# 		num_guess -= 1


#print("You guessed!")

# i = 0
# user_score = 0
# while i<=5:
# 	a = random.randint(1,3)
# 	b = int(input("Please input your guess: "))
# 	if a == b:
# 		user_score +=1
		
# 	i += 1
# print(f"your score is {user_score}")
# 	
user_check = "y"
rounds = 0
user_score = 0
while user_check == "y":
	
	b = int(input("Please input your guess: "))
	a = random.randint(1,3)
	if a == b:
		user_score +=1
		
	user_check = input("do you want to play again: y for yes: ")
	rounds += 1

print(f"your score is {user_score} you have played {rounds} times")
