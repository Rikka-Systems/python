# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import pyautogui as gui
	from time import sleep

	def check_discard():
		if gui.locateOnScreen('./discard.png', confidence=threshold):
			gui.doubleClick(945, 1019)

	# Load the existing PNG image
	but_resolve = './resolve.png'

	# Define a threshold for a "match"
	threshold = 0.95  # You may need to adjust this value

	# Define loop delay between captures
	sleep_time = .25

	while True:
		check_discard()
		gui.click(1776, 948)

		sleep(sleep_time)

else:
	# Code here executed when imported (As a module)
	pass
