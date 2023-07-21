if __name__ == '__main__':
	print('This is intended to be used as a module')
else:
	import functools
	from rich import print as p
	from rich.panel import Panel

	def debug(func):
		@functools.wraps(func)
		def wrapper_debug(*args, **kwargs):
			args_repr = [repr(a) for a in args]
			kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
			signature = ', '.join(args_repr + kwargs_repr)
			p(Panel.fit(f'Calling {func.__name__}({signature})'))
			value = func(*args, **kwargs)
			p(Panel.fit(f'{func.__name__!r} returned {value!r}'))
			return value
		return wrapper_debug
