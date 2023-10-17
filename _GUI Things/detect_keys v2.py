# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import keyboard

	# Define a function to handle key presses
	def check_hotkey(e):
		# Check if Control, Shift, and 'C' keys are pressed
		if e.event_type == keyboard.KEY_DOWN and keyboard.is_pressed('ctrl+shift+c'):
			print("Hello, World!")
		else:
			print('fuck you')


	# Add a hotkey listener
	keyboard.hook(check_hotkey)

	# Keep the script running
	keyboard.wait('esc')  # You can change 'esc' to another key to exit the script

	# Remember to call keyboard.unhook_all() when done to release the keyboard hook.
	keyboard.unhook_all()

else:
	# Code here executed when imported (As a module)
	pass
