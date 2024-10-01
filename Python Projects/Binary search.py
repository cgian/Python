# implementing a Binary Search algorithm in Python to efficiently search for a target value in a sorted list

def binary_search(seq,target_n):

    # "seq" argument is the sequence to examine, target_n argument is the target number we are looking for

    begin_index = 0
    end_index = len(seq) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = seq[midpoint]
        if target_n == midpoint_value:
            return midpoint
        
        elif target_n < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

# ask user for sequence and target value
sequence_a = list(map(int, input('enter integers separated by spaces: ').split()))
target_n = int(input('enter the value to search: '))

# assign result of the binary search to a variable
result = binary_search(sequence_a,target_n)

# check the result
if result == None:
    print(f'target value {target_n} not found in the sequence')
else:
    print(f'target value {target_n} found at index {result}')

