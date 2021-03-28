#EvenOrOdds

"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

"""

num = int(input('pick a number :  '))
check = int(input(f'enter a number to divide by :  '))

if num % check ==0:
    print(f'num is divisible by {check}')
else: 
    print(f'number is not divisible by {check}')
if num % 4 == 0:
    print(f'the number you chose {num} is divisible by 4')
elif num % 2 != 0:
    print(f'the number you chose {num} is odd')
else:
    print(f'the number you chose {num} is even')