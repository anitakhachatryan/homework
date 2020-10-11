import math

#1 

class Circle:

	def __init__(self, radius):
		self.radius = radius

	def area(self):

		area_ = pow(self.radius, 2) * math.pi
		print(f"Area of cirlce with radius {self.radius} is {area_}.")

	def perimeter(self):

		perimeter_ = 2 * self.radius * math.pi
		print(f"Perimeter of a circle with radius {self.radius} is {perimeter_}.")

# cirlce1 = Circle(5)

# cirlce1.area() 
# cirlce1.perimeter()

#2

class array1:

	def __init__(self, array_, target):

		self.array_ = array_
		self.target = target



		for i in range(0, len(self.array_)):
			for j in range(i + 1, len(self.array_)):
				
				if self.array_[i] + self.array_[j] == self.target:

					print(f"indices are: {i}, {j}")


# my_array = array1([10,20,10,40,50,60,70], 50)

class Person:

	def __init__(self, name, surname):

		self.name = name
		self.surname = surname

	def printing(self):

		print(f"name:{self.name}\nsurname:{self.surname}")


class Student(Person):

	def __init__(self, name, surname, faculty):

		Person.__init__(self, name, surname)
		self.faculty = faculty
		
	def student_info(self):

		print(f"{self.name} {self.surname} studies in faculty of {self.faculty}")

# student1 = Student("John", "Brown", "Economics")
# student1.student_info()
# student1.printing()