# sometimes we need our files to be in alphabetical order but when they don't have some zeros at the start of the number, 
# the alphabetical order will sort them in a wrong way. this code solves this by counting the total number of digits in the folder 
# and then by adding the right amount of zeros padding according to that variable
# note: this program works only with the pattern anything_123.anything

import os
import re

# the following function collects in a string the digit it finds after the underscore
def digits_collector(strin):
    new_str=''
    for n in strin:
        try:
            new_str+=str(int(n))
        except:
            None
    return(len(new_str))

#rename file name
def main():
    path = input('enter path (please put \'/\' after the directory): ') # please put '/' after the directory
    print(os.listdir(path))
    
    # the following cicle counts the total number of digits in the folder after the underscore with the help of the previous collector function
    max_digits=0
    for filename in os.listdir(path):
        keyword = re.split('_+', filename)
        if digits_collector(keyword[1]) > max_digits:
            max_digits =  digits_collector(keyword[1])

    print('max digits in folder: ', max_digits)
        
    # in the following cycle we first split the files and calculate the number of zeros needed
    for filename in os.listdir(path):
        keyword = re.split('_+', filename)
        print('old file:')
        print('_'.join(keyword))
        num_zeros_to_ins = max_digits-digits_collector(keyword[1])
        zeros_to_ins=''
        for x in range(0,num_zeros_to_ins):
            zeros_to_ins += '0'
        print('zeros to insert: '+ zeros_to_ins)
        keyword[1] = zeros_to_ins + keyword[1]
        print('new file:')
        print('_'.join(keyword))

    # then we rename the files accordingly
        renamed_file = '_'.join(keyword)
        source = path + filename
        destination = path + renamed_file
        os.rename(source, destination)
        print("Renamed Successfully")

main()