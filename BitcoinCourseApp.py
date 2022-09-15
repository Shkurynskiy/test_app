import math

def convert():
    bp = float(input("What is Bitcoin price today? "))
    while bp <= 0:
        print('Bitcoin price must be greater than zero.')
        bp = float(input("What is Bitcoin price today? " ))
    ds = float(input("How much $ do you have? "))
    while ds < 0:
        print('Please enter an amount greater than 0.')
        ds = float(input("How much $ do you have? " ))
    sum = ds / bp
    print("You can buy,", sum)

convert()
while True:
    flag = input('Repeat calculation? [y/n]: ')
    if flag == 'y':
        convert()
    else:
        break
