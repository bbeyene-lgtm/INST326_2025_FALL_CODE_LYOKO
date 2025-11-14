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
    
    """
    Validates a players guess in a word hunt game 
    
    Parameters:
        guess(str): The word guessed by the user 
        word_list(set): The set of valid words for the current topic ot round.
        guessed_words(set): The set of words the player has already guessed 
        
    Returns: 
        tuple: (is_valid, message)[].
        is_valid (bool): True is the guess is valid and new, False otherwise. 
        message(str): Explanation of the result
    """
    
    if not isinstance(guess, str) or not guess.strip():
        return False, "Invalid input. Please enter a word,"
    
    normalized_guess = guess.strip().lower 
    
    if normalized_guess in guessed_words: 
        return False, f"You already guessed '{normalized_guess}'.Try another new word."
    
    if normalized_guess not in word_list: 
        return False, f"'{normalized_guess}' is not a valid word for this round."
    
    guessed_words.add(normalized_guess)

    return True, f"'{normalized_guess}' is a valid word."
