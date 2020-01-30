inv = []
keys = 1
baton = 2
def guard_room():
    
    print('You are in the Guard room, you see a open locker on one side of the room, and a sleeping guard on the other')
    print()
    r1 = input('What do you do? ')
    while r1 not in ('go to locker','exit room','look'):
        print()
        print('Theres no time for that')
        print()
        r1 = input('What do you do? ')
    while r1 == 'look':
        print()
        print('You are in the Guard room, you see a open locker on one side of the room and a sleeping guard on the other')
        print()
        r1 = input('What do you do? ')
    while r1 == 'exit':
        print()
        print('Cant go back, got to escape')
        print()
        r1 = input('What do you do? ')
    if r1 == 'go to locker':
        print()
        print('You peek in the locker and you see a few batons and a pair of keys')
        print()
        lock_1 = input('What do you do? ')
    if lock_1 == 'take baton':
        inv.append(baton)
        print()
        print('You have taken the baton')
        print()
        print('Out of the conner of your eye you see a door that says WARDENS OFFICE')
        print()
        enter_wo = input('Would you like to enter? ')
        if enter_wo == 'yes':
            print()
            wardens_office()
        elif enter_wo == 'no':
            print()
            print('Oh no, the guard is waking up')
            print()
            print('I hope you have a baton')
            print()
            defend = input('what will you do? ')
            if defend == 'use baton':
                inv.remove(2)
                print('The guard is out you now have time to escape')
            else:
                print('Game Over')
    elif lock_1 == 'take keys':
        inv.append(keys)
        has_key = True
        print()
        print('You have taken the keys')
        print()
        print('Out of the conner of your eye you see a door that says WARDENS OFFICE')
        print()
        enter_wo = input('Would you like to enter? ')
        while lock_1 not in ('take baton','take keys'):
            print()
            print('Theres no time for that')
            print()
            lock_1 = input('What do you do? ')
            print()
            if lock_1 == 'take baton':
                inv.append(baton)
                print()
                print('You have taken the baton')
                print()
                print('Out of the conner of your eye you see a door that says WARDENS OFFICE')
                print()
                enter_wo = input('Would you like to enter? ')
                if enter_wo == 'yes':
                    print()
                    wardens_office()
                elif enter_wo == 'no':
                    print()
                    print('Oh no, the guard is waking up')
                    print()
                    print('I hope you have a baton')
                    defend = input('what will you do? ')
                    if defend == 'use baton':
                        inv.remove(2)
                        print('The guard is out you now have time to escape')
                    else:
                        print('Game Over')
                        while enter_wo not in ('yes','no'):
                            print()
                            print('Theres no time for that')
                            print()
                            enter_wo = input('What do you do? ')
                            if enter_wo == 'yes':
                                print()
                                wardens_office()
                            elif enter_wo == 'no':
                                print()
                                print('Oh no, the guard is waking up')
                                print()
                                print('I hope you have a baton')
                                defend = input('what will you do? ')
                            if defend == 'Use baton':
                                print()
                                inv.remove(2)
                                print('The guard is out you now have time to escape')
                                w
                            else:
                                print('Game Over')

        if enter_wo == 'yes':
            print()
            wardens_office()
        elif enter_wo == 'no':
            print()
            print('Oh no, the guard is waking up')
            print()
            print('I hope you have a baton')
            print('Game Over')
        while enter_wo not in ('yes','no'):
            print()
            print('Theres no time for that')
            print()
            enter_wo = input('What do you do? ')
            if enter_wo == 'yes':
                print()
                wardens_office()
            elif enter_wo == 'no':
                print()
                print('Oh no, the guard is waking up')
                print()
                print('I hope you have a baton')
                print('Game Over')

guard_room()

