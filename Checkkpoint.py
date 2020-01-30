def checkpoint():

    print('You have arrvied at the CHECKPOINT you will finilly be free')
    print()
    print('you just need to scan your key card and you will be free')
    print()
    be_free = input('Scan? ')
    while be_free not in ('yes','no'):
        print()
        print('No time for that')
        print()
        be_free = input('Scan? ')
    if be_free == 'yes':
        print()
        print('You have scanned the card and now you are free')
        inv.remove(3)
    elif be_free == 'no':
        print()
        print('You feel a sudden jolt and you instantly faint')
        print()
        print('Game Over')
##    while be_free not in ('yes','no'):
##        be_free = input('Scan? ')
##        if be_free == 'yes':
##            print()
##            print('You have scanned the card and now you are free')
##            inv.remove(3)
##        elif be_free == 'no':
##            print()
##            print('You feel a sudden jolt and you instantly faint')
##            print()
##            print('Game Over')

checkpoint()
