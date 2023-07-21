import datetime


def date(): return datetime.datetime.now()


start_time = date()

pi0 = 3.141592653589793
pi1 = 0
decimals = 4
term_count = 1

term = 1
denom = 1
add = False

for x in range(14):
	while str(pi1)[:decimals] != str(pi0)[:decimals]:
		denom += 2
		if not add:
			add = True
			term = term - (1 / denom)
		else:
			add = False
			term = term + (1 / denom)
		pi1 = term * 4
		term_count += 1

	print(f"\npi to {decimals - 2} decimals:\t{str(pi1)[:decimals]:>17}")
	print(f"Total terms:\t\t{term_count:>17,}")
	print(f"Time elapsed:\t\t{str(date() - start_time):>17}")
	decimals += 1
