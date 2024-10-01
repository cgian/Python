# game in which user guesses a random number

import random
range_start=int(input('insert the first number of the range '))
range_end=int(input('insert the last number of the range '))
x=random.randint(range_start,range_end)
print('number: ',x)
for attempt in range(1,6):
    y=int(input('guess the number '))
    if x==y:
        print('you won!')
        break
    elif attempt==4:
        print('wrong, last chance')
    elif attempt==5:
        print('you lost!')
    else:
        print('wrong, try again')