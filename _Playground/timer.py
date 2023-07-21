if __name__ == '__main__':
	print('This is intended to be used as a module')
else:
	import time
	import functools
	from rich import print as p
	from rich.panel import Panel

	def timer(func):
		@functools.wraps(func)
		def wrapper_timer(*args, **kwargs):
			start_time = time.perf_counter()
			value = func(*args, **kwargs)
			end_time = time.perf_counter()
			run_time = end_time - start_time
			p(Panel.fit(f'Finished {func.__name__!r} in {run_time:.4f} secs'))
			return value
		return wrapper_timer
