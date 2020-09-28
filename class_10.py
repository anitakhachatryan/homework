a = input("give me pos num: ")

try:
	if not a.isdigit():
		raise ValueError(f"{a} is not a digit")
	a = int(a)
	if a < 0:
		raise Exception("the number could not be negative")
except ValueError as error:
	print(error)
	a = input("give me positive NUMBER ")
except Exception as e:
	print(e)
	a = input("give me POSITIVE number ")

print("value of a is: {}".format(a))