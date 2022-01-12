# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:20:39 2021

@author: dgibb
"""

""" Three main functions:
        main(): runs the overall game
        getSecretNum(): generates the number to guess
        getClues(): collects guesses and evaluates them  
    
    """

import random

max_guesses = 10

def main():
    print(""" This is the bagels game. You have to guess a number from  3 to 10 digits. You can choose the length, but you only get 10 guesses. The number will be made up of digits from 0 to 9 and each digit will only appear once.
          
 When I say:    That means:
 Pico           One digit is correct but in the wrong place.
 Fermi          One digit is correct and in the right place.
 Bagels         No digit is correct.  

So, for example, "pico pico fermi" would mean that two guesses are the right numbers, but in the wrong place, and one guess is correct.          
          """)
          
    while True:
        num_digits = int(input("How long should the number be from 3 digits to 10?\n"))
        if num_digits not in list(range(3,11)):
            print('Choose a number between 3 and 10.')
            continue
        else:
            break
    
    while True:
        secretNum = getSecretNum()
        print("I have thought of a number.")
        ######## HERE #####

    


def getSecretNum():
    # need to generate a random 3-digit number where each digit is only represented once
    # length has to be 10 digits or less
    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNum = ''
    for x in range(num_digits):
        secretNum += numbers[x]
