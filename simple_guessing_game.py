# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:48:14 2020

@author: Titus Newton
"""

import random

balance = 0
play_again = True
print('*'*21)
print('Number Guessing Game.')
print('*'*21)
name = input('Enter your Name: ')
while play_again:
    if balance < 5:
        amount = int(input(f'Welcome {name},Kindly recharge with min 5 Rs/game or more to play the game: '))
        balance+= amount
    else:
        balance -= 5
        print('Rs. 5 deducted and remaining balance is',balance)
        c_guess = random.randint(1,10)
        for chance in range(1,4):
            print() # for an empty line
            print(f'chance: {chance} out of 3')
            print('-'*20)
            u_guess = int(input('Enter a guess in between 1 and 10: '))
            if c_guess == u_guess:
                print(f'Congratz {name} you have guessed correctly and')
                if chance == 1:
                    print('You have won 100 Rs.')
                    balance += 100
                elif chance == 2:
                    print('You have won 75 Rs.')
                    balance += 75
                else:
                    print('You have won 50 Rs.')
                    balance += 50
                break
            else:
                print(f'Sorry {name}, a wrong guess')
                if chance < 3:
                    if u_guess < c_guess:
                        print('I am thinking of a bigger number')
                    else:
                        print('I am thinking of a smaller number')
                else:
                    print('I was thinking of a number',c_guess)
        choice = input('Do you wanna play again [yes/no]: ')
        if choice != 'yes':
            play_again = False
            withdraw = input('Do you wanna withdraw amount [yes/no]: ')
            if withdraw == 'yes' and balance > 0:
                print(f'Available balance is {balance}')
                withdraw_amt = int(input('Enter amount to withdraw: '))
                if withdraw_amt <= balance:
                    print(f'{withdraw_amt} Rs. transferred to your bank a/c')
                    balance -= withdraw_amt
                else:
                    print('Insufficient balance')
            else:
                print('Insufficient balance')
            if balance > 0:
                print(f'Thanks {name} for your donation of Rs. {balance}')