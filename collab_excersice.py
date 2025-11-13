print("One Piece is the best anime ever!") #Aggrey
print("Aric is a jerk (Joking, spare me)") #Lizandro 
print("I love cats") #Johana
print("lets skip this exam!!") #Beimnet


import sys
import argparse


def countingLetters():
    pass

#Input validation and string matching 
def input_validation (guess, word_list, guessed_words):
    if not isinstance(guess, str) or not guess.strip():
        return False, "Invalid input. Please enter a word,"
    
    normalized_guess = guess.strip().lower 
    
    if normalized_guess in guessed_words: 
        return False, f"You already guessed' '{normalized_guess}'. Try a new word."