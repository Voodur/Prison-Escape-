inv = []

keys = 1
baton = 2
key_card = 3


if inv == [1]:
    print('You have, Keys')
elif inv == [2]:
    print('You have, Baton')
elif inv == [3]:
    print('You have, Key Card')
elif inv == [1,2]:
    print('You have, Keys, Baton')
elif inv == [2,3]:
    print('You have, Baton, Key Card')
elif inv == [1,3]:
    print('You have, Keys, Key Card')


locked_door = input('What to use? ')
if locked_door ==  'Keys' or locked_door == 'keys':
    inv.remove(1)
    print('You have used the Keys')

print(inv)
