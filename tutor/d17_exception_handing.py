try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2021 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
