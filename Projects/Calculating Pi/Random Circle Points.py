import random as rd
import datetime


def date(): return datetime.datetime.now()


start_time = date()

pi0 = 3.141592653589793
pi1 = 0
decimals = 4
point_in = total_points = 0

for x in range(14):
	while str(pi1)[:decimals] != str(pi0)[:decimals]:
		x = rd.random()
		y = rd.random()
		total_points += 1
		if (x * x + y * y) ** 0.5 <= 1: point_in += 1
		pi1 = 4 * point_in / total_points

	print(f"\npi to {decimals - 2} decimals:\t{str(pi1)[:decimals]:>17}")
	print(f"Total points:\t\t{total_points:>17,}")
	print(f"Time elapsed:\t\t{str(date() - start_time):>17}")
	decimals += 1
