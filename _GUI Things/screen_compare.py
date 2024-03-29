# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import cv2
	import numpy as np
	import pyautogui
	import time

	# Load the existing JPG image
	existing_image = cv2.imread('./sample.png')

	# Define a threshold for a "match"
	threshold = 0.95  # You may need to adjust this value

	# Define loop delay between captures
	sleep_time = 1

	while True:
		# Set region of capture
		screen_width, screen_height = pyautogui.size()
		x_start, y_start = 0, 0
		x_end, y_end = screen_width, screen_height

		# Capture screen region defined above
		screenshot = pyautogui.screenshot(region=(x_start, y_start, x_end, y_end))
		screenshot = np.array(screenshot)
		screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

		# Try to find the existing image in the screenshot
		result = cv2.matchTemplate(screenshot, existing_image, cv2.TM_CCOEFF_NORMED)

		# Find the locations where the match is above the threshold
		locations = np.where(result >= threshold)

		if len(locations[0]) > 0:
			print("Match")
		else:
			print("No Match")

		# Wait for time before taking the next screenshot
		time.sleep(sleep_time)

else:
	# Code here executed when imported (As a module)
	pass
