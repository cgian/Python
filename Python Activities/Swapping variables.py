# swapping numbers either by using a 3rd variable or in one go

first_num = input ('enter the first number ')
second_num = input ('Enter the second number ')
third_var = None
while True:
    method=input('enter 1 to swap the numbers through a 3rd variable, enter 2 to swap them in one go ')
    if method=='1':
        third_var=first_num
        first_num=second_num
        second_num=third_var
        print('first number now is: ',first_num)
        print('second number now is: ',second_num)
        print('third variable (',third_var,') was used')
        break
    elif method=='2':
        first_num, second_num = second_num, first_num
        print('first number now is: ',first_num)
        print('second number now is: ',second_num)
        print('third variable (',third_var,') was not used')
        break