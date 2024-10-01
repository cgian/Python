# Basic Calculator able to perform Addition, Subtraction, Multiplication and Division

def div(a,b):
    try:
        result=a/b
        print('result: ',result)
    except ZeroDivisionError:
        print('division for zero is impossible')

def sub(a,b):
    result=a-b
    print('result: ',result)

def mult(a,b):
    result=a*b
    print('result: ',result)

def add(a,b):
    result=a+b
    print('result: ',result)

err_msg='wrong entry, the operands must be numeric'
import sys
next_operation=False
while True:
    x=input('enter the first operand: ')
    try:
        x=float(x)
    except:
        print(err_msg)
        continue
    y=input('enter the second operand: ')
    try:
        y=float(y)
    except:
        print(err_msg)
        continue
    while True:
        operation=input('what operation would you like to perform? enter: \n1 for addition \n2 for subtraction\n3 for multiplication\n4 for division\n')
        lol=1
        if operation=='1':
            add(x,y)
        elif operation=='2':
            sub(x,y)
        elif operation=='3':
            mult(x,y)
        elif operation=='4':
            div(x,y)
        else:
            print('wrong entry, choice must be a number between 1 and 4')
            continue
        while True:
            next=input('do you want to perform another operation? yes/no: ')
            if next=='no':
                sys.exit()
            elif next=='yes':
                next_operation=True
                break
            else:
                print('wrong entry, choice should be yes or no')
                continue
        if next_operation:
            break
