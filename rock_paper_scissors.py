"""
Game of rock, paper scissors
Python 3.8.5

"""
from random import choice
from sys import exit

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

play_dict = {'r': 'ROCK',
             'p': 'PAPER',
             's': 'SCISSORS'}

game_dict = {'win': [['r', 's'], ['s', 'p'], ['p', 'r']],
             'loss': [['s', 'r'], ['p', 's'], ['r', 'p']]}


while True:  # Main game loop.

    while True:  # Player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit.')
        print('{0} Wins, {1} Losses, {2} Ties'.format(wins, losses, ties))

        computer = choice('rps')
        play = input()
        if play == 'q':
            print('See you next time...')
            exit()

        # Display what player chose:
        print('{} versus...'.format(play_dict.get(play)))

        # Display what computer chose:
        print(play_dict.get(computer))

        # Display and record the win/loss/ties
        if computer == play:
            print('It is a tie!\n')
            ties += 1
        elif [play, computer] in game_dict['win']:
            print('You won! Next time you gonna be smashed!\n')
            wins += 1
        elif [play, computer] in game_dict['loss']:
            print('You lost, as usual!\n')
            losses += 1
