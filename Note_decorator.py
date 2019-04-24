
def log(func):
	def wrapper(*args, **kw):
		print('call %s(): ' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def stop():
	print('stop')

stop()


def logging(text):
	def decorator(func):
		def wrapper(*args, **kwargs):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kwargs)
		return wrapper

	return decorator

@logging('execute')
def now():
	print('1234556')

now()

print(now.__name__)

import functools

def print_log(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		print('call %s()' % func.__name__)
		return func(*args, **kwargs)

	return wrapper

@print_log
def run_log():
	print_log('run')

run_log()

print(run_log.__name__)


def log(something):
    # if callable, this is a decorator, shape of @log
    if callable(something):
        func = something
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call {}'.format(func.__name__))
            func(*args, **kwargs)
        return wrapper

    elif isinstance(something, str):
        # else, this is a decorator function, shape of @log(something)
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print('{} {}'.format(something, func.__name__))
                func(*args, **kwargs)
            return wrapper

        return decorator

    else:
        raise AttributeError("Attribute other than str is not supported")

@log
def f():
    pass

@log('execute')
def f2():
    pass

f()
f2()

print(f.__name__)
print(f2.__name__)