# Program that finds the Zodiac Sign of people based on their date of birth; data will be stored in a CSV file using Pandas

import pandas as pd
import os
import os.path

while True:
    name = input('enter name: ')
    year = input('enter year of birth: ')
    month = input('enter month of birth: ')
    day = int(input('enter day of birth: '))

    #region - sign calculation (lines folded: expand to see them)
    if month == 'january':
        if day <= 19:
            sign = 'capricorn'
        else:
            sign = 'aquarius'
    if month == 'february':
        if day <= 18:
            sign = 'aquarius'
        else:
            sign = 'pisces'
    if month == 'march':
        if day <= 20:
            sign = 'pisces'
        else:
            sign = 'aries'
    if month == 'april':
        if day <= 19:
            sign = 'aries'
        else:
            sign = 'taurus'
    if month == 'may':
        if day <= 20:
            sign = 'taurus'
        else:
            sign = 'gemini'
    if month == 'june':
        if day <= 21:
            sign = 'gemini'
        else:
            sign = 'cancer'
    if month == 'july':
        if day <= 22:
            sign = 'cancer'
        else:
            sign = 'leo'
    if month == 'august':
        if day <= 22:
            sign = 'leo'
        else:
            sign = 'virgo'
    if month == 'september':
        if day <= 22:
            sign = 'virgo'
        else:
            sign = 'libra'
    if month == 'october':
        if day <= 23:
            sign = 'libra'
        else:
            sign = 'scorpio'
    if month == 'november':
        if day <= 21:
            sign = 'scorpio'
        else:
            sign = 'sagittarius'
    if month == 'december':
        if day <= 21:
            sign = 'sagittarius'
        else:
            sign = 'capricorn'
    #endregion

    print(f'new entry: {name}, born {day} {month} {year}, sign: {sign}')

    # here we check whether the list we use is already present, if not, we create it
    if 'zodiac_data' in locals():
        None
    else:
        zodiac_data = []

    # here we add the new entry as a dictionary into the list
    zodiac_data.append({
        'name': name ,'year': year, 'month': month, 'day': day, 'sign': sign
    })

    # asking the user if they want to add another entry
    while True:
        continuation = input('do you want to add another entry? (yes/no) ')
        if continuation in ['yes','no']:
            break
        else:
            print ('wrong answer')
    if continuation == 'no':
        break
    else:
        None

# printing the list
print(zodiac_data)

# assigning the list to the dataframe data argument
df = pd.DataFrame(data=zodiac_data)

# asking the user for the path
path = input('enter the path for csv file: (please include "/" at the end) ')+'zodiac data.csv'

# note: the file will either be updated or created, we check if such file exists at the location to determine what to do
if os.path.isfile(path):
    df.to_csv(path, mode='a', header=False)
else:
    df.to_csv(path)

print(df)

print('data successfully added to csv file "zodiac data" in your specified directory')

