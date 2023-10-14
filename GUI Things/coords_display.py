# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import pyautogui
	import time

	def print_cursor_coordinates():
		while True:
			x, y = pyautogui.position()
			print(f"Cursor Position: x = {x}, y = {y}")
			time.sleep(0.5)

	try:
		print("Press Ctrl-C to stop the script.")
		print_cursor_coordinates()
	except KeyboardInterrupt:
		print("Script terminated by user.")

else:
	# Code here executed when imported (As a module)
	pass
