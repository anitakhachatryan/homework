import threading
import concurrent.futures
import time
import json
import requests


info = {
	"items": [
		{
			"name": "python_image",
			"url": "https://business.blogthinkbig.com/wp-content/uploads/sites/2/2019/04/Pythonlogo.jpg"
		},
		{
			"name": "multithreading_image",
			"url": "https://d33wubrfki0l68.cloudfront.net/068a31a66053ff64f78184d971196829cf927fba/c892f/wp-content/uploads/2017/07/multithreading.png"
		},
		{
			"name": "Italy image1",
			"url": "https://images.unsplash.com/photo-1515859005217-8a1f08870f59?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
		},
		{
			"name": "Italy image2",
			"url": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=333&q=80"
		},
		{
			"name": "Italy image3",
			"url": "https://images.unsplash.com/photo-1516108317508-6788f6a160e4?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
		},
		{
			"name": "Italy image4",
			"url": "https://images.unsplash.com/photo-1518204213685-466b68a6d0f8?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
		},
		{
			"name": "Hawaii image1",
			"url": "https://lp-cms-production.imgix.net/2019-06/c05b829af5ee38ab1917f335d937f8e1-hawaii.jpg?auto=format&fit=crop&ixlib=react-8.6.4&h=520&w=1312&q=75&dpr=1"
		},
		{
			"name": "Hawaii image2",
			"url": "https://www.exoticca.com/uk/magazine/wp-content/uploads/2019/05/The-12-most-spectacular-beaches-in-hawaii-that-you-cannot-miss-930x360.jpg"
		},
		{
			"name": "Hawaii image3",
			"url": "https://cdn.travelpulse.com/images/54aaedf4-a957-df11-b491-006073e71405/ee952e9e-f09c-49c2-bc5d-4303c880173a/630x355.jpg"
		},
		{
			"name": "Hawaii image4",
			"url": "https://specials-images.forbesimg.com/imageserve/5e086b074e29170007841c94/960x0.jpg?cropX1=0&cropX2=2121&cropY1=107&cropY2=1300"
		}
	]
}
# n
# for value in info.values():
# 	for i in range(10):
# 		print(value[i], end = "\n")
	


if __name__ == '__main__':

	def downloader(range_num):
		rename = "images"
		with open("new_sample_json.json", "r") as links:
			link_list = json.load(links)
		
		
		for value in info.values():
			for i in range(range_num):
				response = requests.get(value[i]["url"])
				with open(rename + ".jpeg", "wb") as image:
					image.write(response.content)
					rename += "b"

				print(rename)

			return "downloaded!"


	thread_list = []
	
	for j in range(4):
		
		x = threading.Thread(target = downloader, args =(10,), daemon = True)
		thread_list.append(x)
		x.start()
	

	for thread in thread_list:
		thread.join()
	

# downloader()