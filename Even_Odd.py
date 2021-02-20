import random

name = input('What is your name: ')
print('Welcome', name,', Please pick a number between 1 to 1000')
print('What number are you thinking')
num = int(input())

ran = random.randint(1,1000)
print(ran)
if ran % num == 0:
    print('This is an even number')
else:
    print('That is an Odd number')
