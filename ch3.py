## guess a number
import random

guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 20)
print('Well, ' + myName + ' I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):  # guessesTaken is i
    print('You have %s chances left...\n Take a guess :)' % (6 - guessesTaken))
    try:
        guess = int(input())
    except:
        print('wrong input, please input an integer')
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    # guessesTaken = str(guessesTaken)
    print('Good job, %s ! You guess my number in %s guesses!' % (myName, guessesTaken + 1))

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was %s' % number)
