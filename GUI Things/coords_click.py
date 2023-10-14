# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import pyautogui

	# Define the coordinates where you want to click
	x, y = 500, 500  # Change these values to the desired coordinates

	# Move the mouse to the specified coordinates and click
	pyautogui.click(x, y)


else:
	# Code here executed when imported (As a module)
	pass
