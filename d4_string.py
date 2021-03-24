# Strings

# Creating a String

letter = 'p'
print(letter)

# String Concatenation

first_name = 'Air'
last_name = 'Keith'
space = ' '
full_name = first_name + space + last_name
print(full_name)

# String formating
# Old Style `% Operator`
pi = 3.1415926
formated_string = 'I am %s %s, you can call me %.2f' % (
    first_name, last_name, pi)
print(formated_string)

# New Style 1 `str.format()`
new_formated_string = 'I am {} {}, you can call me {}'.format(
    first_name, last_name, pi)
print(new_formated_string)

# New Style 2 `f-Strings` (Python 3.6+)
print(f'I am {first_name} {last_name}, you can call me {pi}')

# Reversing a String
print(first_name[::-1])
