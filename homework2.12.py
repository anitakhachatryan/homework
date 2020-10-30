import logging
import random


logging.basicConfig(filename = "random_nums.log", format = '%(asctime)s:%(levelname)s:%(message)s', level = logging.DEBUG)
for i in range(50):
	num = random.randint(0,50)

	if num < 10:
		logging.debug(f"Number generated is {num} and is in range 0 - 9")
	elif num >= 10 and num < 20 :
		logging.info(f"Number generated is {num} and is in range 10 - 19")
	elif num >= 20 and num < 30:
		logging.warning(f"Number generated is {num} and is in range 20 - 29")
	elif num >= 30 and num < 40:
		logging.error(f"Number generated is {num} and is in range 30 - 39")
	else:
		logging.critical(f"Number generated is {num} and is in range 40 - 50")