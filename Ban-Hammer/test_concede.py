# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import pyautogui as gui
	from time import sleep

	gui.click(1882, 34)
	sleep(.065)
	gui.mouseDown(955, 631)
	sleep(.001)
	gui.mouseUp()
	sleep(4)
	gui.click()

else:
	# Code here executed when imported (As a module)
	pass
