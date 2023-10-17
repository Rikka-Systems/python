if __name__ == '__main__':
	pass
else:
	# Code here executed when imported (As a module)
	import pyautogui as gui
	from time import sleep

	def concede():
		gui.click(1882, 34)
		sleep(.1)
		gui.mouseDown(955, 631)
		sleep(.001)
		gui.mouseUp()
		sleep(4)
		gui.click()
		return
