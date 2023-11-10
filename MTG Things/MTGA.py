# Code here is always executed
import random

from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import pyautogui as gui
	import keyboard
	from time import sleep
	import os

	def concede():
		but_bored = './buttons/bored.png'
		gui.click(959, 809)
		sleep(0.1)
		while True:
			if gui.locateOnScreen(but_bored, confidence=0.95):
				gui.mouseDown(878, 697)
				sleep(.001)
				gui.mouseUp()
				gui.click(1882, 34)
				sleep(.1)
				gui.mouseDown(955, 631)
				sleep(.001)
				gui.mouseUp()
				sleep(4)
				gui.click()
				break
			else:
				gui.mouseDown(1356, 781)
				sleep(.001)
				gui.mouseUp()
		return

	def check_banned(mode_state):
		if mode_state:
			pass
		else:
			return
		cards_path = './cards'
		cards = [file for file in os.listdir(cards_path) if file.lower().endswith(".png")]
		for card in cards:
			if gui.locateOnScreen(f'{cards_path}/{card}', confidence=0.90):
				concede()
				sleep(1)
		return

	def auto_draft(mode_state):
		if mode_state:
			pass
		else:
			return
		if gui.locateOnScreen('./buttons/draft.png', confidence=0.95):
			draft_pick = random.randint(1, 3)
			match draft_pick:
				case 1:
					gui.mouseDown(630, 476)
					sleep(.001)
					gui.mouseUp()
				case 2:
					gui.mouseDown(955, 476)
					sleep(.001)
					gui.mouseUp()
				case 3:
					gui.mouseDown(1287, 476)
					sleep(.001)
					gui.mouseUp()
		return

	def auto_play(mode_state):
		if mode_state:
			pass
		else:
			return
		if gui.locateOnScreen('./buttons/play.png', confidence=0.90):
			gui.mouseDown(1738, 1003)
			sleep(.001)
			gui.mouseUp()
		if gui.locateOnScreen('./buttons/claim.png', confidence=0.90):
			gui.mouseDown(1738, 1003)
			sleep(.001)
			gui.mouseUp()
		return


	play_toggle = False
	draft_toggle = False
	ban_toggle = False
	while True:
		auto_play(play_toggle)
		auto_draft(draft_toggle)
		check_banned(ban_toggle)

		# Press 0 to concede
		if keyboard.is_pressed('0'):
			concede()

		# Press 1 to toggle autoplay
		if keyboard.is_pressed('1'):
			sleep(.2)
			if play_toggle:
				play_toggle = False
			else:
				play_toggle = True
			print(f'Autoplay Mode: {play_toggle}')

		# Press 2 to toggle autodraft
		if keyboard.is_pressed('2'):
			sleep(.2)
			if draft_toggle:
				draft_toggle = False
			else:
				draft_toggle = True
			print(f'Autodraft Mode: {draft_toggle}')

		# Press 9 to toggle banned card checking
		if keyboard.is_pressed('9'):
			sleep(.2)
			if ban_toggle:
				ban_toggle = False
			else:
				ban_toggle = True
			print(f'Ban Mode: {ban_toggle}')

else:
	# Code here executed when imported (As a module)
	pass
