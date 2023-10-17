# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import time
	import pygetwindow as gw

	while True:
		try:
			active_window = gw.getActiveWindow()
			window_title = active_window.title
			print("Active Window Title:", window_title)
		except AttributeError:
			# Handle the case when no active window is found
			print("No active window")
		time.sleep(1)  # Check every 1 second


else:
	# Code here executed when imported (As a module)
	pass
