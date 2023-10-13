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
	existing_image = cv2.imread('C:\\Users\\Loki\\Documents\\ShareX\\Screenshots\\2023-10\\hammer.jpg')

	# Define a threshold for a "match"
	threshold = 0.35  # You may need to adjust this value

	while True:
		# Take a screenshot of the left half of your 1080p monitor
		screen_width, screen_height = pyautogui.size()
		left_half_width = screen_width // 2
		top_half_height = screen_height // 2

		# Capture the left half of the screen
		screenshot = pyautogui.screenshot(region=(0, 0, left_half_width, top_half_height))
		screenshot = np.array(screenshot)
		screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

		# Try to find the existing image in the screenshot
		result = cv2.matchTemplate(screenshot, existing_image, cv2.TM_CCOEFF_NORMED)

		# Find the locations where the match is above the threshold
		locations = np.where(result >= threshold)

		if len(locations[0]) > 0:
			print("hammer time")
		else:
			print("No match found")

		# Wait for half a second before taking the next screenshot
		time.sleep(1)

else:
	# Code here executed when imported (As a module)
	pass
