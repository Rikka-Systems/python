import time
from rich import print as p
from rich.prompt import IntPrompt
import random as rd
from rich.table import Table
from rich import box


def main():
	if (door_count := IntPrompt.ask('How many doors?')) < 2:
		exit('Game requires 2 or more doors')

	prizes = ['winner']
	for _ in range(door_count - 1):
		prizes.append('loser')

	stay_win = stay_loss = 0
	rounds = rd.randrange(1_000_000, 5_000_000)

	print('Running simulation. Please wait...')

	start = time.perf_counter()
	for _ in range(rounds):
		rd.shuffle(prizes)
		if prizes[rd.randrange(0, door_count)] == 'winner':
			stay_win += 1
		else:
			stay_loss += 1
	finish = time.perf_counter()
	print(f'Simulation finished in {round(finish - start, 2)} seconds\n')

	# Calculations
	switch_win = stay_loss
	switch_loss = stay_win
	stay_percent_win = switch_percent_loss = stay_win / rounds
	stay_percent_loss = switch_percent_win = stay_loss / rounds

	# Results
	print(f'Results from {rounds:,} rounds:')

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
	return


if __name__ == '__main__':
	start_ = time.perf_counter()
	main()
	finish_ = time.perf_counter()
	print(f'\nFinished in {round(finish_ - start_, 2)} seconds')
