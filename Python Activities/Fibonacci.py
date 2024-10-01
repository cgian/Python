while True:
    n=int(input('enter the fibonacci length '))
    counter=0
    a=0
    b=1
    if n<3:
        print('a fibonacci sequence must be at least 3 numbers long')
    else:
       for n in range(0,n):
            x=a+b
            print(a)
            a=b
            b=x
