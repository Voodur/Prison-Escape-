inv = [1]

def visitors_center():

    print('You have left the wardens office and entered a room that looks like a visitors center.')
    print('You can see 4 doors in the room, 1 stratght north of you, 1 to the east, 1 to the west and 1 right south you leading back into the office.')
    print()
    r3 = input('Which door should you enter? ')
    while r3 not in ('look','n','e','s','w'):
        print()
        print('No time for that')
        print()
        r3 = input('Which door should you enter? ')
    while r3 == 'look':
        print()
        print('You have left the wardens office and entered a room that looks like a visitors center.')
        print('You can see 4 doors in the room, 1 stratght north of you, 1 to the east, 1 to the west and 1 right south you leading back into the office.')
        print()
        r3 = input('Which door should you enter? ')
    if r3 == 'n':
        print()
        print('The door is locked')
        print()
        use_key = input('What will you do? ')
        while use_key not in ('turn back','use key'):
              print()
              print('No time for that')
              print()
              use_key = input('What will you do? ')
        if use_key == 'use key':
            print()
            if inv == [1]:
                print('You enter the north door')
 #               checkpoint()
                inv.remove(1)
            elif not inv == [1]:
                print('You dont have the keys')
                print()
                print('The guard is here')
                print()
                print('Game Over')
        elif use_key == 'turn back':
            print()
            print('You turn around and see a guard walking towards you')
            print()
            print('Game Over')
    elif r3 == 'e':
        print()
        print('You enter the east door')
        waiting_room()
    elif r3 == 'w':
        print()
        print('You enter the west door')
        office()
    while r3 == 's':
        print()
        print('No time to retrace my steps')
        print()
        r3 = input('Which door should you enter? ')
##        while r3 == 'look':
##            print()
##            print('You have left the wardens office and entered a room that looks like a visitors center.')
##            print()
##            print('You can see 4 doors in the room, 1 stratght north of you, 1 to the east, 1 to the west and 1 right south you leading back into the office.')
##        if r3 == 'n':
##            print()
##            if inv == [1]:
##                print('You enter the north door')
##                checkpoint()
##                inv.remove(1)
##            elif not inv == [1]:
##                print('You dont have the keys')
##                print()
##                print('The guard is here')
##                print()
##                print('Game Over')
##        elif r3 == 'e':
##            print()
##            print('You enter the east door')
##            waiting_room()
##        elif r3 == 'w':
##            print()
##            print('You enter the west door')
##            office()
##        while r3 == 's':
##            print()
##            print('No time to retrace my steps')

#visitors_center()


    
##        while r3 == 'look':
##            print('You have left the wardens office and entered a room that looks like a visitors center.')
##            print()
##            print('You can see 4 doors in the room, 1 stratght north of you, 1 to the east, 1 to the west and 1 right south you leading back into the office.')
##        if r3 == 'n':
##            print()
##            if has_key == True:
##                print('You enter the north door')
##                checkpoint()
##                inv.remove(1)
##            elif has_key == False:
##                print('The door is locked')
##                print()
##                print('You turn around and see a guard walking towards you')
##                print()
##                print('Game Over')
##        elif r3 == 'e':
##            print()
##            print('You enter the east door')
##            waiting_room()
##        elif r3 == 'w':
##            print()
##            print('You enter the west door')
##            office()
##        elif r3 == 's':
##            print()
##            print('No time to retrace my steps')
##            print()
##            r3 = input('Which door should you enter? ')
##            while r3 == 'look':
##                print('You have left the wardens office and entered a room that looks like a visitors center.')
##                print()
##                print('You can see 4 doors in the room, 1 stratght north of you, 1 to the east, 1 to the west and 1 right south you leading back into the office.')
##            if r3 == 'n':
##                print()
##                if has_key == True:
##                    print('You enter the north door')
##                    checkpoint()
##                    inv.remove(1)
##                elif has_key == False:
##                    print('The door is locked')
##                    print()
##                    print('You turn around and see a guard walking towards you')
##                    print()
##                    print('Game Over')
##            elif r3 == 'e':
##                print()
##                print('You enter the east door')
##                waiting_room()
##            elif r3 == 'w':
##                print()
##                print('You enter the west door')
##                office()
##            elif r3 == 's':
##                print()
##                print('No time to retrace my steps')

visitors_center()



        
