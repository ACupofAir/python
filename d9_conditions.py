# Conditions
username = input('What\'s your name?\n')
if isinstance(username, str):
    print(f'Hello, {username}!')
else:
    print('Error: Please ensure input your right name!')

userage = int(input('What\'your age?\n'))
if userage > 0:
    if userage > 18:
        print('You can married')
    else:
        print('You are too young to marry someone')
elif userage == 0:
    print('Are your sure?')
else:
    print('Your age is negative, It must be wrong.')
