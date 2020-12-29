from random import choice


number = choice(range(1, 21))
print('I am thinking of a number between 1 and 20.')
print(number)


for guesses_taken in range(1, 7):
    guess = int(input('Take a guess.\n'))
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    print('Good job! You guessed my number in {} guesses!'
          .format(guesses_taken))
else:
    print('Nope. The number I was thinking of was {}.'.format(number))
