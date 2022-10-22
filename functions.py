# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:27:07 2022

@author: rahma
"""

from word_list import word_list
import random

def getWord():
    word = random.choice(word_list)
    return word

def display(user_letters, word):
    display_letter =""
    for letter in word:
        if letter in user_letters:
            display_letter += letter 
        else:
            display_letter += "-"
    return display_letter

def play():
    word = getWord()
    word_letters = set(word)
    user_letters = ""
    print(f"I thought of a word with {len(word)} letters, can you guess?")
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Letters you have found so far: {user_letters}")
        letter = input("Type letter>>  ")
        if  letter in user_letters:
            print("We already have this letter")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} letter is correct.")
        else:
            print("Try again, this letter is not in the word.")
        user_letters += letter 
    print(f"Congrats, you have found {word} word in {len(user_letters)} shots.")