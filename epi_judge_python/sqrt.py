def fixed_point(func, first_guess):
	def close_enough(v1, v2):
			return abs(v1 - v2) < 0.00001
	def try_again(guess):
		next_val = func(guess)
		if close_enough(next_val, guess):
			return next_val
		else:
			return try_again(next_val)
	return try_again(first_guess)

def square(x):
	return x*x

def average(x, y):
	return (x+y)/2

def fixed_point_of_transform(g, transform, guess):
	return fixed_point(transform(g), guess)

def average_damp(f):
	return lambda x: average(x, f(x))

def sqrt(x):
	return fixed_point_of_transform(lambda y: x/y, average_damp, 1)

def cbrt(x):
	return fixed_point_of_transform(lambda y: x/square(y), average_damp, 1)

print(sqrt(25))

print(cbrt(27))