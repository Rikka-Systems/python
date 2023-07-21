# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	my_dict = {
		"key01": {
			"key02": 42
		}
	}
	my_dict["key01"]["key02"] += 1
	print(my_dict["key01"]["key02"])

else:
	# Code here executed when imported (As a module)
	pass
