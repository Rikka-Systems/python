# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)

	def update_results(*args):
		with open('Results.txt', 'a') as results_file:
			results_file.write(f'{args[0]}={args[1]}\n')
		return

	def return_false():
		return False

	def return_true():
		return True

	code = "test01"
	update_results(code, return_true())

	code = "test02"
	update_results(code, return_false())

else:
	# Code here executed when imported (As a module)
	pass
