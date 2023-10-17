# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import keyboard
	from MTGA_Concede import concede

	# Define a function to handle key presses

	def get_key():
		while True:
			try:
				event = keyboard.read_event()
				if event.event_type == keyboard.KEY_DOWN:
					print(f'Keypress: {event.name}')
					return event.name
			except KeyboardInterrupt:
				break

	while True:
		match get_key():
			case '1':
				concede()
			case 'f':
				print('Boredom Mode')
			case _:
				pass

else:
	# Code here executed when imported (As a module)
	pass
