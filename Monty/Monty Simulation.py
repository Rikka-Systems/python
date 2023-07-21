# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	from rich.prompt import IntPrompt
	from rich.table import Table
	from rich import box
	from rich import print as p
	import random as rd

	def play_round(doors):
		prizes = ['winner']
		for _ in range(doors - 1):
			prizes.append('loser')
		rd.shuffle(prizes)
		if prizes[rd.randrange(0, door_count)] == 'winner':
			return "win"
		else:
			return "loss"


	if (door_count := IntPrompt.ask('How many doors?')) < 2:
		exit('Game requires 2 or more doors')
	else:
		stay_win = stay_loss = 0
		rounds = 1_000_000
		for _ in range(rounds):
			result = play_round(door_count)
			if result == "win":
				stay_win += 1
			else:
				stay_loss += 1

			# Calculations
			switch_win = stay_loss
			switch_loss = stay_win
			stay_percent_win = switch_percent_loss = stay_win / rounds
			stay_percent_loss = switch_percent_win = stay_loss / rounds

		# Results
		print(f'Results from {rounds:,} rounds and {door_count:,} doors:')

		table = Table(box=box.SIMPLE)
		table.add_column('')
		table.add_column('Percent', justify='right')
		table.add_column('')
		table.add_column('Totals', justify='right')

		table.add_row('Results if stay:')
		table.add_row('Wins', f'{stay_percent_win:.3%}', 'Total:', f'{stay_win:,}')
		table.add_row('Losses', f'{stay_percent_loss:.3%}', 'Total:', f'{stay_loss:,}')

		table.add_row('\nResults if switch:')
		table.add_row('Wins', f'{switch_percent_win:.3%}', 'Total:', f'{switch_win:,}')
		table.add_row('Losses', f'{switch_percent_loss:.3%}', 'Total:', f'{switch_loss:,}')

		p(table)


else:
	# Code here executed when imported (As a module)
	pass
