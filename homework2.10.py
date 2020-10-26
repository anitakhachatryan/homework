import requests

# class Image:

# 	def __init__(self, image_list):

# 		self.image_list = image_list

# 	def download_png(self):

# 		name = "photo"

# 		with open(self.image_list, "r") as file:
# 			for line in file:
# 				# print(line)

# 				response = requests.get(line)
# 				with open(name+".png", "wb") as file:   #can be .jpeg, since source is jpeg format
# 					file.write(response.content)
# 					name += "a"

# 	def donwload_jpeg(self):

# 		name = "photo"

# 		with open(self.image_list, "r") as file:
# 			for line in file:
# 				# print(line)

# 				response = requests.get(line)
# 				with open(name+".jpeg", "wb") as file:   #can be .jpeg, since source is jpeg format
# 					file.write(response.content)
# 					name += "b"

# image = Image('photos.txt')

# image.download_png()
# image.donwload_jpeg()


# --- with 2 classes ---
class Png:

	def __init__(self, images):
		self.images = images

	def download(self):
		name = "photo"

		with open(self.images, "r") as file:
			for line in file:
				# print(line)

				response = requests.get(line)
				with open(name+".png", "wb") as file:   #can be .jpeg, since source is jpeg format
					file.write(response.content)
					name += "a"

class Jpeg:

	def __init__(self, images):
		self.images = images

	def download(self):
		name = "photo"

		with open(self.images, "r") as file:
			for line in file:
				# print(line)

				response = requests.get(line)
				with open(name+".jpeg", "wb") as file:   #can be .jpeg, since source is jpeg format
					file.write(response.content)
					name += "b"

photos = Png('photos.txt')

photos2 = Jpeg('photos.txt')

photos.download()
photos2.download()