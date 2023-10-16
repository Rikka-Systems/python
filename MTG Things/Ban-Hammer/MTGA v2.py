# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import pyautogui as gui
	from time import sleep

	# Load the existing JPG image
	banned_card = './hammer.png'

	# Define a threshold for a "match"
	threshold = 0.90  # You may need to adjust this value

	# Define loop delay between captures
	sleep_time = 1

	def concede():
		gui.click(1882, 34)
		sleep(.065)
		gui.mouseDown(955, 631)
		sleep(.001)
		gui.mouseUp()
		sleep(4)
		gui.click()

	while True:
		if gui.locateOnScreen(banned_card, confidence=threshold):
			print("Match")
			concede()
		else:
			print("No Match")

		# Wait for time before taking the next screenshot
		sleep(sleep_time)

else:
	# Code here executed when imported (As a module)
	pass
