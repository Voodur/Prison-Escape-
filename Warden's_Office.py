#Wardens Office
inv = []
key_card = 3

def wardens_office():
    
    print('You are now in the Wardens Office')
    print()
    print('On one side of the room you see a unlocked locker, and on the other side of the room you see the Wardens Desk')
    print()
    r2 = input('What would you like to do? ')
    while r2 not in ('go to locker','go to desk','look'):
        print()
        print('Theres no time for that')
        print()
        r2 = input('What would you like to do? ')
    while r2 == 'look':
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
        while take_card not in ('yes','no'):
            print()
            print('Theres no time for that')
            print()
            take_card = input('Take it? ')
        if take_card == 'yes':
            inv.append(key_card)
            has_key_card = True
            print()
            print('You have taken the Master Key')
            print()
        while take_card == 'no':
            print()
            print('I will not get far without this, I should take it')
            print()
            take_card = input('Take it? ')
            if take_card == 'yes':
                inv.append(key_card)
                has_key_card = True
                print()
                print('You have taken the Master Key')
                print()
        print('Now that I have the key I should head to the check point')
        print()
        print('You leave the office and enter a room that looks like the VISITORS CENTER')
        print()
        visitors_center()
        #vistors_center()
##    while r2 not in ('go to locker','go to desk','look'):
##        print()
##        print('Theres no time for that')
##        print()
##        r2 = input('What would you like to do? ')
##        while r2 == 'look':
##            print('On one side of the room you see a unlocked locker, and on the other side of the room you see the Wardens Desk')
##            r2 = input('What would you like to do? ')
##    if r2 == 'go to locker':
##        print()
##        print('You walk over to the locker and open it')
##        print()
##        print('Oh no its a motion alarm')
##        print()
##        print('The guards are on their way')
##        print()
##        print('Game Over')
##    elif r2 == 'go to desk':
##        print()
##        print('You walk over to the desk')
##        print()
##        print('You see a card on the table that says MASTER KEY, You think to yourself  This is my way out') 
##        print()
##        take_card = input('Take it? ')
##        if take_card == 'yes':
##            inv.append(key_card)
##            has_key_card = True
##            print()
##            print('You have taken the Master Key')
##        while take_card == 'no':
##            print()
##            print('I will not get far without this, I should take it')
##            print()
##            take_card = input('Take it? ')
##            if take_card == 'yes':
##                inv.append(key_card)
##                has_key_card = True
##                print()
##                print('You have taken the Master Key')
##                print()
##        print('Now that I have the key I should head to the check point')
##        print()
##        print('You leave the office and enter a room that looks like the VISITORS CENTER')
##        #visitors_center()
        

            
        
     

wardens_office()


