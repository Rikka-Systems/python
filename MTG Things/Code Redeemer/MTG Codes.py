# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	from time import sleep
	import pyautogui as gui

	but_ok = './MTG_ok.png'
	code_list = open('./codes.txt')
	redeemed_list = open('./redeemed.txt')

	with code_list:
		codes = [line.strip() for line in code_list.readlines()]

	with redeemed_list:
		redeemed = [line.strip() for line in redeemed_list.readlines()]

	for code in codes:
		if code in redeemed:
			print(f'Code: {code} already redeemed')
			continue

		gui.click(1760, 121)
		gui.hotkey('ctrl', 'a')
		gui.press('del')
		gui.write(f'{code}\n')

		_ = True
		while _:
			try:
				gui.mouseDown(but_ok)
				sleep(.001)
				gui.mouseUp()
				_ = False
			except:
				pass

		sleep(1)

else:
	# Code here executed when imported (As a module)
	pass
