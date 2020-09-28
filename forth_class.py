# decides whether the num is odd or even

# num = int(input("Please input number: "))
# even = num % 2 == 0
# odd = num % 2 == 1
# print("It is even: ", even)
# print("It is odd:", odd)


#decide what to do based on weather

# weather = input("What's the weather/raining or shining: ")

# if (weather == "raining"):
# 	print("Take an umbrella!")
# elif (weather == "shining"):
# 	print("Take your sunglasses!")
# else:
# 	print("Do what you want.")

# print("I just wanted to help!")


# takes three numbers, returns the max one
# num1 = int(input("Please input number 1: "))
# num2 = int(input("Please input number 2: "))
# num3 = int(input("Please input number 3: "))

# if num1 > num2 and num1 > num3:
# 	print(num1, " is the biggest one")
# elif num2 > num1 and num2 > num3:
# 	print(num2, " is the biggest one")
# else:
# 	print(num3, " is the biggest one")

#version 2 -- nested if
num1 = int(input("Please input number 1: "))
num2 = int(input("Please input number 2: "))
num3 = int(input("Please input number 3: "))

if num1 > num2:
	if num1 > num3:
		print(num1, " is the biggest one")
	else:
		#num3 > num2
		print(num3,"is the biggest")
elif num2 > num3:
	print(num2, " is the biggest one")
	
else:
	print(num3, " is the biggest one")

