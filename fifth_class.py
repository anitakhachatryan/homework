# check from 2d till 4th letters = ing or not, return message

# text = input("please input word: ")
# print(text[1:4] == "ing")
#if text[1:4] == "ing":
	#print("ing is on it's place")
# else:
# 	print("try again")
# text2 = "ly"
# length = len(text) - 3
# if text[-3:] == "ing":
# 	print(text[:length]+text2)


# changes found letter to 0 and prints new word
# word = "playing"
# letter = input("please input letter to find ")
# len1 = word[:word.find(letter)]
# len2 =  word[word.find(letter) + 1:]
# if letter in word:
# 	print(len1+"0"+len2)
# print(len1)
# print(len2)


# isalpha / isdigit / find digit in string

# string = input("please input string: ")
# num_in_string = 0
# print(string.find(str(num_in_string)))

# if string.isdigit():
# 	print("its number")

# if string.isalpha():
# 	print("its string")

# formatting / placeholders

my_text = "My name is {fname}, I'm {age}.".format(fname = "Anita", age = 26)
my_text2 = "My name is {0}, I'm {1}.".format("Anita", 26)
my_text3 = "My name is {}, I'm {}.".format("Anita", 26)