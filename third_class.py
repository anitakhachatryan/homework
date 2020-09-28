# circle_radius = float(input("Input circle radius "))
# p = 3.14
# circle_area = p*(circle_radius**2)

#print(circle_area)

# name = input("What's your name:\n")
# surname = input("What's your surname:\n")
# print(surname, name)

#asks for age, calculates when will be 100 y.o.

from datetime import datetime
current_age = int(input("Whats your age now:\n"))
current_date = datetime.now()
current_year = current_date.year
calculate_100 = 100 - current_age + current_year
print(calculate_100)

