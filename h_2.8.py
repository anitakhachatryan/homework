import os


os.chdir("/Users/Admin/Desktop/Python/2/new_folder/new_folder2")
path = os.getcwd()



while path != "/Users/Admin/Desktop/Python/2":


	path = os.getcwd()
	print(path)
	list_ = os.listdir(os.getcwd())
	list1 = list_[0]

	print(list1)

	os.removedirs(list1)

	os.chdir("..")
	