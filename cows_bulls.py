import random

number = []

for num in range (4):
	num = random.randint(0,9)
	number.append(num)

while (number[0] == number[1] or number[0] == number[2] or number[0] == number[3]\
or number[1] == number[2] or number[1] == number[3] or number[2] == number[3]):
	number.clear()
	for num in range (4):
		num = random.randint(0,9)		
		number.append(num)
print(number)

games = 0

def game():
	global games
	cows = 0
	bulls = 0
	games += 1
	user_number_ = []	
	user_number = input("Please enter 4 digit number/ with different digits: ")
	for f in range(4):
		user_number_.append(int(user_number[f]))
	for i in range(4):
		for j in range(4):
			if user_number_[i] == number[j]:
				bulls += 1
	for k in range(4):
		if user_number_[k] == number[k]:
			cows += 1
	
	print(f"cows: {cows}\nbulls: {bulls}")	
	
	if cows == 4:
		print(f"You won after {games} games.")

	if cows != 4:
		game()

game()
