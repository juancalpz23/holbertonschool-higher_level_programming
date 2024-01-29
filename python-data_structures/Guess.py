#!/usr/bin/python3
import random
def guess_game():
    rand_num = random.randint(1, 20)
    guess = None

    while guess != rand_num:
        guess = int(input('Guess a number between 1 and 20: '))
        if guess < rand_num:
            print('Higher')
        elif guess > rand_num:
            print('Lower')
        else:
            print('You WIN!')
    guess_game()
guess_game()