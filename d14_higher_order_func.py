# Function as a Parameter

def sum_numbers(nums):
    return sum(nums)


def higher_sum(f, *args):
    summation = f(*args)
    return summation


print(higher_sum(sum_numbers, [1, 2, 3, 4]))

# Function as a Return Value


def square(x):
    return x**2


def cube(x):
    return x**3


def absolute(x):
    if x >= 0:
        return x
    else:
        return (-x)


def higher_calculate(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


result = higher_calculate('square')
print(result(3))


# Python Closures


def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add


closure_result = add_ten()
print(closure_result(5))


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
# > greeting = uppercase_decorator(greeting)
def greeting():
    return 'Welcome to Python'


print(greeting())


# Build in Functions
# > map(func, iterable)
numbers = [1, 2, 3, 4, 5]
number_squared = map(lambda x: x**2, numbers)
print(list(number_squared))


# > filter(func, iterable)


def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_number = filter(is_even, numbers)
print(list(even_number))
