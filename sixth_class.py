# a = int(input("Please input number for multiplication table: "))

# for i in range(1, 11):
# 	print("{} x {} = {}".format(a, i, a*i))


year = int(input("Please input year: "))

sum_of_digit = 0
for i in range(0, 4):
	num = year % 10
	year //= 10
	sum_of_digit += num

print(sum_of_digit)

# 2nd vers of prev
#  a = input("num")
#  b= 0
#  for i in a:
#  	b += int(i)
#  print(b)

# a = input("date:")
# b = 0
# for i in a:
# 	if i.isdigit()
# 	b += i

# print(b)

#calculate sum of (1,20), but exclude x % 3 == 0

#z = 0 #sum of nums
# for j in range(1,21):
# 	if j % 3 == 0:
# 		continue
# 	else: 
# 		z += j
# print(z)
# 2nd vers of prev
# y = 0
# for  k in range(1,21):
# 	z += k
# for l in range(1,21):
# 	if l % 3 == 0:
# 		y += l
# print(z-y)

#calculate sum of (1,20) and stop when reach 15

# d = 0
# for e in range(1,21):
# 	m = e - 1
# 	if d >= 15:
# 		g = d - e
# 		break
# 	else:
# 		d += e
# if (14 - g >= d - 14):
# 	print(d)
# else:
# 	print(g)

# print(d, m)
 # the same but a bit more nice
# s = 0
# j = 15
# for i in range(1,21):
# 	s += i
# 	if s > j:
# 		break
# print("s= ", s)
# a = s - i
# if j - a > s - j:
# 	print("s= ", s)
# else:
# 	print("s= ", a)


#given a str, display only those chars which are present at an even index num

# string = input("Please input text:\n")
# h = 0
# for o in string:
# 	h = string[0]
# 	h += 1

# 	if string[h] % 2 == 0:
# 		print(o)

