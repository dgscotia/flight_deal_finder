# -*- coding: utf-8 -*-
"""
Created on Sun Sep 5 23:04:47 2021

@author: dgibb
"""

"""
How does the program work? It has 3 functions. 
main(): runs the overall game. It's the function that's run to start everything else.
secretNum(): generates the number you should guess.
getClues(): collects the guesses and evaluates them.
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Duncan's recreation of the bagels game.
          
 I am thinking of a {} digit number with no repeated digits. Try to guess what it is.
          
 When I say:    That means:
 Pico           One digit is correct but in the wrong place.
 Fermi          One digit is correct and in the right place.
 Bagels         No digit is correct.          
          '''.format(NUM_DIGITS))
          

    while True:
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('No more guesses.')
                print('The correct answer was {}.'.format(secretNum))
                
        print('Play again? (Yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')
            
def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
            
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
           
if __name__ == '__main__':
    main()     
        
        
        
        
        