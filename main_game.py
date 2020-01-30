inv = []

keys = 1
baton = 2
key_card = 3

def cell():
#starting position
    print('You wake up in your cell, the doors are open')
    print()
    m1 = input('What would you like to do ? ')
    while m1 == 'look':#loops room discription
        print()
        print('You wake up in your cell, the doors are open')
        print()
        m1 = input('What would you like to do ? ')
    if m1 == 'exit cell':
        print()
        hallway()#calls next room
    elif m1 == 'sleep':
        print()
        print('Goodnight')
        print()
        print('You will be released in 2 years')
    while m1 not in ('look','exit cell','sleep'):# loops if user input is invalid
        print()
        print('Theres no time for that')
        print()
        m1 = input('What do you do? ')
        while m1 == 'look':
            print()
            print('You wake up in your cell, the doors are open')
            print()
            m1 = input('What would you like to do ? ')
        if m1 == 'exit cell':
            print()
            hallway()#calls next room
        elif m1 == 'sleep':
            print()
            print('Goodnight')
            print()
            print('You will be released in 2 years')
    
def hallway():
    
    print('You are now in the Hallway')
    print()
    print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
    print()
    m2 = input('What would you like to do ? ')
    while m2 == 'look':#loops room discription
        print()
        print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
        print()
        m2 = input('What would you like to do ? ')
    while m2 == 's':
        print()
        print('Cant go back to my cell now, I have to escape')
        print()
        m2 = input('What would you like to do ? ')
        while m2 == 'look':# loops the room discription
            print()
            print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
            print()
            m2 = input('What would you like to do ? ')
    while m2 == 'e':
        print()
        print('Their is a wall blocking your way ')
        print()
        m2 = input('What would you like to do ? ')
        while m2 == 'look':#loops room discription
            print()
            print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
            print()
            m2 = input('What would you like to do ? ')
            while m2 == 's':
                print()
                print('Cant go back to my cell now, I have to escape')
                print()
                m2 = input('What would you like to do ? ')
    if m2 == 'w':
        print()
        print('You have entered the GUARD ROOM')
        print()
        guard_room()
    elif m2 == 'n':
        print()
        print('You have run into the guard!!')
        print()
        print('Game Over')

def guard_room():
    
    print('You are in the Guard room, you see a open locker on one side of the room, and a sleeping guard on the other')
    print()
    r1 = input('What do you do? ')
    while r1 not in ('go to locker','exit room','look'):#loops if user input is invalid
        print()
        print('Theres no time for that')
        print()
        r1 = input('What do you do? ')
    while r1 == 'look':#loops room discription
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
        inv.append(baton)# adds item to invintory
        print()
        print('You have taken the baton')
        print()
        print('Out of the conner of your eye you see a door that says WARDENS OFFICE')
        print()
        enter_wo = input('Would you like to enter? ')
        if enter_wo == 'yes':
            print()
            wardens_office()#calls next room
        elif enter_wo == 'no':
            print()
            print('Oh no, the guard is waking up')
            print()
            print('I hope you have a baton')
            print()
            defend = input('what will you do? ')
            if defend == 'use baton':
                inv.remove(2)#removes item from inventory
                print('The guard is out you now have time to escape')
            else:
                print('Game Over')
    elif lock_1 == 'take keys':
        inv.append(keys)#adds item to invintory
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
                inv.append(baton)#adds item to inventory
                print()
                print('You have taken the baton')
                print()
                print('Out of the conner of your eye you see a door that says WARDENS OFFICE')
                print()
                enter_wo = input('Would you like to enter? ')
                if enter_wo == 'yes':
                    print()
                    wardens_office()#calls next room
                elif enter_wo == 'no':
                    print()
                    print('Oh no, the guard is waking up')
                    print()
                    print('I hope you have a baton')
                    defend = input('what will you do? ')
                    if defend == 'use baton':
                        inv.remove(2)#removes item form inventory
                        print('The guard is out you now have time to escape')
                    else:
                        print('Game Over')
                        while enter_wo not in ('yes','no'):#while user input is invalid, will loop
                            print()
                            print('Theres no time for that')
                            print()
                            enter_wo = input('What do you do? ')
                            if enter_wo == 'yes':
                                print()
                                wardens_office()#calls next room
                            elif enter_wo == 'no':
                                print()
                                print('Oh no, the guard is waking up')
                                print()
                                print('I hope you have a baton')
                                defend = input('what will you do? ')
                            if defend == 'Use baton':
                                print()
                                inv.remove(2)#removes item from inventory
                                print('The guard is out you now have time to escape')
                                wardens_office()#calls next room
                            else:
                                print('Game Over')

        if enter_wo == 'yes':
            print()
            wardens_office()#calls next room
        elif enter_wo == 'no':
            print()
            print('Oh no, the guard is waking up')
            print()
            print('I hope you have a baton')
            print('Game Over')
        while enter_wo not in ('yes','no'):#while user input is invalid, will loop
            print()
            print('Theres no time for that')
            print()
            enter_wo = input('What do you do? ')
            if enter_wo == 'yes':
                print()
                wardens_office()#calls next room
            elif enter_wo == 'no':
                print()
                print('Oh no, the guard is waking up')
                print()
                print('I hope you have a baton')
                print()
                print('Game Over')


def wardens_office():
    
    print('You are now in the Wardens Office')
    print()
    print('On one side of the room you see a unlocked locker, and on the other side of the room you see the Wardens Desk')
    print()
    r2 = input('What would you like to do? ')
    while r2 not in ('go to locker','go to desk','look'):#while user input is invalid, will loop
        print()
        print('Theres no time for that')
        print()
        r2 = input('What would you like to do? ')
    while r2 == 'look':#loops room discription
        print()
        print('On one side of the room you see a unlocked locker, and on the other side of the room you see the Wardens Desk')
        print()
        r2 = input('What would you like to do? ')
        print()
    if r2 == 'go to locker':
        print()
        print('You walk over to the locker and open it')
        print()
        print('Oh no its a motion alarm')
        print()
        print('The guards are on their way')
        print()
        print('Game Over')
    elif r2 == 'go to desk':
        print()
        print('You walk over to the desk')
        print()
        print('You see a card on the table that says MASTER KEY, You think to yourself  This is my way out') 
        print()
        take_card = input('Take it? ')
        while take_card not in ('yes','no'):#while user input is invalid, will loop
            print()
            print('Theres no time for that')
            print()
            take_card = input('Take it? ')
        if take_card == 'yes':
            inv.append(key_card)#adds item to invintory
            print()
            print('You have taken the Master Key')
            print()
        while take_card == 'no':
            print()
            print('I will not get far without this, I should take it')
            print()
            take_card = input('Take it? ')
            if take_card == 'yes':
                inv.append(key_card)#adds item to invintory
                print()
                print('You have taken the Master Key')
                print()
        print('Now that I have the key I should head to the check point')
        print()
        print('You leave the office and enter a room that looks like the VISITORS CENTER')
        print()
        visitors_center()#calls next room

def visitors_center():

    print('You have left the wardens office and entered a room that looks like a visitors center.')
    print('You can see 4 doors in the room, 1 stratght north of you, 1 to the east, 1 to the west and 1 right south you leading back into the office.')
    print()
    r3 = input('Which door should you enter? ')
    while r3 not in ('look','n','e','s','w'):#while user input is invalid, will loop
        print()
        print('No time for that')
        print()
        r3 = input('Which door should you enter? ')
    while r3 == 'look':#loops room discription
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
        while use_key not in ('turn back','use key'):#while user input is invalid, will loop
              print()
              print('No time for that')
              print()
              use_key = input('What will you do? ')
        if use_key == 'use key':
            print()
            if inv == [1]:
                print('You enter the north door')
                checkpoint()#calls next room
                inv.remove(1)# removes item from inventory
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
        waiting_room()# calls next room
    elif r3 == 'w':
        print()
        print('You enter the west door')
        office()#calls next room
    while r3 == 's':
        print()
        print('No time to retrace my steps')
        print()
        r3 = input('Which door should you enter? ')
        
def waiting_room():

    print('You enter the WAITING ROOM and you see mutilpe guards just waiting to take you  back to your cell')
    print()
    print('You have no chance')
    print()
    print('Game Over')

def office():

    print('You enter a room that looks like an office')
    print()
    print('Just your luck, a group of guards have spotted you')
    print()
    print('Game Over')


def checkpoint():

    print('You have arrvied at the CHECKPOINT you will finilly be free')
    print()
    print('you just need to scan your key card and you will be free')
    print()
    be_free = input('Scan? ')
    while be_free not in ('yes','no'):#loops if user input is invalid
        print()
        print('No time for that')
        print()
        be_free = input('Scan? ')
    if be_free == 'yes':
        print()
        print('You have scanned the card and now you are free')
        inv.remove(3)# removes item from inventory
    elif be_free == 'no':
        print()
        print('You feel a sudden jolt and you instantly faint')
        print()
        print('Game Over')
        





cell()
