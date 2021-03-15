# Function suing keyworld def
# It's  need two blank lines after a function
# * Function with Parameters
def greetings(name):
    message = f'Hello, {name}'
    return message


print(greetings('Keith Air'))

def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)


generate_groups('Team-1', 'Air', 'Thunder')
