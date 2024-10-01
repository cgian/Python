# this code renames the files by sorting them first in the correct way.
# just alphabetically they would be sorted like file1,file10,file2... which is wrong

import os
import re

path = input('enter path (please put \'/\' after the directory): ') # please put '/' after the directory
print(os.listdir(path))
new_name = input('what name do you want to give to your files? ')

# this function takes the numbers in a string and combines them creating an integer than can be used for a proper sorting
def int_converter(name_to_conv):
    name_to_conv=int(''.join([n for n in name_to_conv if n.isdigit()]))
    return name_to_conv

def main():

    print('original unsorted file list:',os.listdir(path))
    # storing the file names in a list
    list_files=os.listdir(path)
    # the following line will sort the files using the previously created function
    list_files.sort(key=int_converter)
    print('properly sorted file list: ',list_files)

    filecounter=0
    for filename in list_files:
        print('original file name: '+ filename)
        # with the split method we keep the file extension
        split_filename = re.split('([.])', filename)
        filecounter += 1
        renamed_file = new_name + str(filecounter) + split_filename[1] + split_filename[2]
        print('new file name: ' + renamed_file)
        
        # now that we have the new file name, let's rename the file

        source = path + filename
        destination = path + renamed_file
        os.rename(source, destination)
        print('renamed successfully')

main()

