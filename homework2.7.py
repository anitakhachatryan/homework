class Heating:

	def __init__(self, bedroom_current_temp, bathroom_current_temp, \
		bedroom_goal_temp, bathroom_goal_temp):

		# global bedroom_current_temp, max_current_temp, bedroom_goal_temp, max_goal_temp

		self.__bedroom_current_temp = bedroom_current_temp
		self.__bathroom_current_temp = bathroom_current_temp
		self.__bedroom_goal_temp = bedroom_goal_temp
		self.__bathroom_goal_temp = bathroom_goal_temp

	def get_temp(self):

		return self.__bedroom_current_temp, self.__bathroom_current_temp,\
		self.__bedroom_goal_temp, self.__bathroom_goal_temp

	def set_temp(self, new_bedroom_current_temp = 0, new_bathroom_current_temp = 0, \
		new_bedroom_goal_temp = 0, new_bathroom_goal_temp = 0):

		self.__bedroom_current_temp = new_bedroom_current_temp
		self.__bathroom_current_temp = new_bathroom_current_temp
		self.__bedroom_goal_temp = new_bedroom_goal_temp
		self.__bathroom_goal_temp = new_bathroom_goal_temp

	def goal_temp_achieved(self):

		if self.__bedroom_current_temp == self.__bedroom_goal_temp:
			print("Current tempreture of bedroom is according to goal tempretures")

		else:
			print("Current tempreture of bedroom varies from goal tempretures. Please review")

		if self.__bathroom_current_temp == self.__bathroom_goal_temp:

			print("Current tempreture of bathroom is according to goal tempretures")
		
		else:
			print("Current tempreture of bathroom varies from goal tempretures. Please review")


	def __str__(self):

		return f"The current temp of bedroom is {self.__bedroom_current_temp} and of bathroom is {self.__bathroom_current_temp}\
 while goal tempretures are set at {self.__bedroom_goal_temp} and {self.__bathroom_goal_temp} respectively."

		

# def checking_temp(list_):
	# count_normal = 0
	# for i in range(4):
	# 	for temps in list_[i]:

	# 		if abs(__bedroom_goal_temp - __bedroom_current_temp) <= 2 and \
	# 		abs(__bathroom_goal_temp - __bathroom_current_temp) <= 2:
	# 			count_normal += 1
		
			# return count_normal


house1 = Heating(15, 18, 22, 26)
house2 = Heating(30, 17, 22, 26)
house3 = Heating(22, 26, 22, 26)
house4 = Heating(25, 35, 22, 26)

list_1 = []

list_1.append(house1)
list_1.append(house2)
list_1.append(house3)
list_1.append(house4)

# print(checking_temp(list_1))
# print(list_1[0])
house2.set_temp(16, 19, 21, 25)
print(house2.get_temp())

house3.goal_temp_achieved()


print(str(house1))
