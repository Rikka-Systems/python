# Code here is always executed
import readline

from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import keyboard

	with open('D:/My Drive/Python/Projects/Lorem Ipsum/LoremIpsum.txt') as lorem:
		lines = 4
