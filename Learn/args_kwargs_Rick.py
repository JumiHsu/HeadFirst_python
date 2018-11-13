# https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
# https://stackoverflow.com/questions/3394835/args-and-kwargs


def wrapper(function, *args, **kwargs):
	return function(*args, **kwargs)

def test1(a, b, c):
	print("a: ", a)
	print("b: ", b)
	print("c: ", c)



print("example 1")
wrapper(test1, 1, 2, 3)

print("example 2")
wrapper(test1, a=1, c=3, b=2)

print("example 3")
wrapper(test1, 3, c=1, b=2)
