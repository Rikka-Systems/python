# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import pyautogui
	import time

	# Load the existing JPG image
	existing_image = './sample.png'

	# Define a threshold for a "match"
	threshold = 0.95  # You may need to adjust this value

	# Define loop delay between captures
	sleep_time = 1

	while True:
		if matched := pyautogui.locateOnScreen(existing_image):
			print(matched)
		else:
			print('None')

		# Wait for time before taking the next screenshot
		time.sleep(sleep_time)

else:
	# Code here executed when imported (As a module)
	pass
