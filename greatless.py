#Write a program to check whether the given number is greater than 15 or smaller than 15.
num = int(input('Type your number: '))
if num > 15:
    print(num, 'is greater than 15')
elif num < 15:
    print(num, 'is less than 15')
else:
    print(num, 'is equal to 15')