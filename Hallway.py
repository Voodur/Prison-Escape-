#Hallway5

def hallway:
print('You are now in the Hallway')
print()
print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
print()
m2 = input('What would you like to do ? ')
while m2 == 'look':
    print()
    print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
    print()
    m2 = input('What would you like to do ? ')
while m2 == 'e':
    print()
    print('Their is a wall blocking your way ')
    print()
    m2 = input('What would you like to do ? ')
    while m2 == 'look':
        print()
        print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
        print()
        m2 = input('What would you like to do ? ')
if m2 == 'w':
    print()
    print('You run into a sign that says GUARD ROOM')
    print()
    enter_ga = input('Would you like to enter? ')
    if enter_ga == 'yes':
        print()
        print('You have entered')
##    elif enter_ga == 'no':
##       print()
##       print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
##       print()
##       m2 = input('What would you like to do? ')

    
if m2 == 's':
    print()
    enter_cell = input('Would you like to go back in your cell? ')
    if enter_cell == 'yes':
        print()
        print('You are back in your cell')
    elif enter_cell == 'no':
        print()
        print('The Hallway is almost pitch black, you know the guard is somewhere but you cant see anything')
    
elif m2 == 'n':
    print()
    print('You have run into the guard!!')
    print()
    print('Game Over')

while not 'n''s''e''w''look':
    m2 = input('What would you like to do ? ')
    
