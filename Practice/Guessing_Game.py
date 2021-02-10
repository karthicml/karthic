from random import randint
a = randint(0,100)
b = float(input('Enter a number between 0 and 100: '))
while b<0 or b>100 or b%1!=0:
        print('OUT OF BOUNDS: enter a whole number between 0 and 100')
        b = float(input('Enter a number between 0 and 100: '))
if a == b:
        pass
elif abs(a-b)<11:
        print('WARM!')
        c = abs(a-b)
        b = float(input('Enter a number between 0 and 100: '))
else:
        print('COLD!')
        c = abs(a-b)
        b = float(input('Enter a number between 0 and 100: '))
        
while a!=b:
    if b<0 or b>100 or b%1!=0:
        print('OUT OF BOUNDS: enter a whole number between 0 and 100')
        b = float(input('Enter a number between 0 and 100: '))
    else:
        if abs(a-b)<c:
            print('WARMER!')
            c = abs(a-b)
            b = float(input('Enter a number between 0 and 100: '))
        else:
            print('COLDER!')
            c = abs(a-b)
            b = float(input('Enter a number between 0 and 100: '))          
print('Bingo')