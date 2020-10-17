class Hotel:
	def __init__(self, name, place, rooms_mid,mid_room_price, rooms_luxe, luxe_room_price):

    	self.name = name
    	self.place = place
    	self.rooms_mid = rooms_mid
    	self.mid_room_price = mid_room_price
    	self.rooms_luxe = rooms_luxe
    	self.luxe_room_price = luxe_room_price
  
	def presentation(self):
    	text = f"This is {self.name} hotel. It is located in {self.place}. Standard and luxe rooms are available. Prices available_room_check {self.mid_room_price} AMD and {self.luxe_room_price} AMD per night respectively."

    	return text

	def booking(self, availability_mid = 0, availability_luxe = 0):

    	# status = input("Do you want to book the room? ")
    	if availability_mid == "book":
        	for key in self.rooms_mid:
            	self.rooms_mid[key] = "booked"

    	if availability_luxe == "book":
        	for key in self.rooms_luxe:
            	self.rooms_luxe[key] = "booked"
      
    	print (self.rooms_mid, self.rooms_luxe)

	def available_room_check(self):

      	for key in self.rooms_mid:
            
          	if self.rooms_mid[key] == "free":
                print(f"room {self.rooms_mid[key]} is free")
          	else:
                  print(f"room {self.rooms_mid[key]} is booked")

      	for key in self.rooms_luxe:

          	if self.rooms_luxe[key] == "free":
                print(f"room {self.rooms_luxe[key]} is free")
          	else:
              	print(f"room {self.rooms_luxe[key]} is booked")

	def discount(self, percent):

  		new_price_mid = self.mid_room_price*(1-percent/100)
  		new_price_luxe = self.luxe_room_price*(1-percent/100)

  		return f"Discounted price for luxe room is {new_price_luxe} AMD per night, for standard room {new_price_mid} AMD per night"

class Taxi:

	def __init__(self, name, car_types, price_for_tour):
		self.name = name
		self.car_types = car_types
		self.price_for_tour = price_for_tour

	def presentation(self):

		text = f"This is {self.name} taxi service. It has {self.car_types} in its carpark."

		return text

	def discount(self, percent):

		new_price = self.price_for_tour*(1-percent/100)

		return new_price

class Tour(Hotel, Taxi):

	def __init__(self, name):

		self.name = name

		# Hotel.__init__(self, name, place, rooms_mid,mid_room_price, rooms_luxe, luxe_room_price)
		# Taxi.__init__(self, name, car_types, price_for_tour)

		# super().__init__
		# self.price_mid = mid_room_price + price_for_tour
		# self.price_luxe = luxe_room_price + price_for_tour

	def presentation(self):

		# super().presentation()
		# Hotel.__init__(self, name, place, rooms_mid,mid_room_price, rooms_luxe, luxe_room_price)
		# Taxi.__init__(self, name, car_types, price_for_tour)


		self.price_mid = mid_room_price + price_for_tour
		self.price_luxe = luxe_room_price + price_for_tour

		text = f"We offer tour to {self.place}. Price for the tour is {self.price_mid} AMD per person per night for standard room and\
		 {self.price_luxe} AMD per person per night for luxe room. This price includes hotel and transportation via {self.name} company\
		 which provides {self.car_types} for price of {self.price_for_tour}. Hotel at the location is {self.name}. Prices are:\
		  {self.mid_room_price} AMD per person per night for standard room and {self.luxe_room_price}MD per person per night for luxe room."

		return text


hotel1 = Hotel("Nairi", "Jermuk", {"room1": "free", "room2":"free", "room3":"booked"}, 20000, {"room1":"booked",\
 "room2":"free", "room3":"free"}, 50000)
# hotel1.booking("book")
# print(hotel1.presentation())
# hotel1.available_room_check()

# print(hotel1.discount(15))
taxi1 = Taxi("city tour", "Toyota", 10000)
# print(taxi1.presentation())
# print(taxi1.discount(10))
tour1 = Tour("Jermuk")
print(tour1.presentation())
