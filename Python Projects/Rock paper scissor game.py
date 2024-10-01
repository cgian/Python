# Creating a Python program that allows the player to play Rock-Paper-Scissors against the computer.
# Through the random module, I generate a random number between 1 and 3, then I allow the user to choose their hand.
# Then, through if statements, I process what should happen in all the cases

import sys
import random

def win():
    print('you won!')
def lose():
    print('you lost!')
def even():
    print('even')

while True:
    x=random.randint(1,3)
    print(x)
    y = 0
    while y not in [1,2,3]:
        try:
            y=int(input('enter: \n1 for rock\n2 for paper\n3 for scissor\n'))
        except:
            None
        if y not in [1,2,3]:
            print('wrong entry')
    if x==y:
        even()
    elif x==1 and y==2:
        win()
    elif x==1 and y==3:
        lose()
    elif x==2 and y==1:
        lose()
    elif x==2 and y==3:
        win()
    elif x==3 and y==1:
        win()
    else:
        lose()
    while True:
        z = input('continue? (yes/no) ')
        if z == 'yes':
            break
        elif z == 'no':
            sys.exit()
        else:
            print('wrong entry')