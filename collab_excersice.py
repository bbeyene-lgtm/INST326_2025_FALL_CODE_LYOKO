import random
from collections import Counter
import sys
import argparse
import time


plants = [word for word in ["trees", "flowers", "shrubs", "herbs", "tulips", "roses", "daisies", "bushes",
          "ferns", "mosses", "cacti", "vines", "grasses", "palms", "sunflowers", "lilies",
          "orchids", "daffodils", "irises", "marigolds", "lavender", "jasmine", "peonies",
          "begonias", "chrysanthemums", "hydrangeas", "azaleas", "camellias", "gardenias", "grasses",
          "bamboo", "succulents", "aloe vera", "sage", "thyme", "rosemary", "basil", "mint", "oregano",
          "cilantro", "parsley", "dill", "fennel", "chives", "lemongrass", "tarragon", "bay leaves",
          "coriander", "lavender", "echinacea", "ginseng", "chamomile", "valerian"] if len(word) <= 10]

animals = [word for word in ["lion", "tiger", "elephant", "giraffe", "zebra", "kangaroo", "panda", "bear",
           "wolf", "fox", "deer", "rabbit", "squirrel", "monkey", "gorilla", "chimpanzee",
           "leopard", "cheetah", "hyena", "rhinoceros", "hippopotamus", "crocodile", "alligator",
           "snake", "lizard", "tortoise", "frog", "toad", "salmon", "trout", "shark",
           "dolphin", "whale", "octopus", "squid", "jellyfish", "crab", "lobster", "shrimp",
           "butterfly", "bee", "ant", "spider", "scorpion", "eagle", "hawk", "owl",
           "parrot", "penguin", "flamingo", "peacock", "swan", "duck", "goose", "turkey",
           "chicken", "rooster", "ostrich", "emu", "platypus", "armadillo", "sloth", "anteater",
           "rabbit", "hamster", "guinea pig", "ferret", "chinchilla", "hedgehog", "meerkat",
           "wombat", "koala", "tasmanian devil", "mole", "vole", "lemming", "weasel", "badger",
           "snake", "gecko", "iguana", "chameleon", "komodo dragon", "newt", "salamander"] if len(word) <= 10]

sports = [word for word in ["soccer", "basketball", "baseball", "tennis", "golf", "cricket",
          "rugby", "hockey", "volleyball", "badminton", "table tennis", "swimming",
          "cycling", "running", "boxing", "wrestling", "skiing", "snowboarding", "skateboarding",
          "surfing", "sailing", "rowing", "fishing", "archery", "fencing", "gymnastics",
          "weightlifting", "yoga", "pilates", "aerobics", "dance", "cheerleading",
          "karate", "judo", "taekwondo", "kickboxing", "mixed martial arts", "triathlon",
          "marathon", "ultramarathon", "hiking", "climbing", "caving", "orienteering",
          "parkour", "bouldering", "curling", "luge", "skeleton", "bobsledding",
          "handball", "water polo", "synchronized swimming", "diving", "triathlon"] if len(word) <= 10]

topicdict = {
    "plants": plants,
    "animals": animals,
    "sports": sports, }


alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




class Grid:
    """
    A word‑search puzzle grid that supports placing words horizontally or vertically
    and filling remaining cells with random letters.
    """

    def __init__(self, rows=10, columns=10):
        """
        Initialize an empty grid.

        Parameters:
            rows (int): Number of rows in the grid.
            columns (int): Number of columns in the grid.
        """
        self.rows = rows
        self.columns = columns
        self.grid = [['' for _ in range(columns)] for _ in range(rows)]
        self.words = []

    def _can_place(self, word, row, col, direction):
        """
        Check whether a word can be placed at a given position.

        Parameters:
            word (str): The word to place.
            row (int): Starting row index.
            col (int): Starting column index.
            direction (str): 'horizontal' or 'vertical'.

        Returns:
            bool: True if placement is valid, otherwise False.
        """
        if direction == 'horizontal':
            if col + len(word) > self.columns:
                return False
            for i in range(len(word)):
                if self.grid[row][col + i] not in ('', word[i]):
                    return False
            return True

        if direction == 'vertical':
            if row + len(word) > self.rows:
                return False
            for i in range(len(word)):
                if self.grid[row + i][col] not in ('', word[i]):
                    return False
            return True

        return False

    def _place(self, word, row, col, direction):
        """
        Place a word into the grid at a valid position.

        Parameters:
            word (str): The word to place.
            row (int): Starting row index.
            col (int): Starting column index.
            direction (str): 'horizontal' or 'vertical'.
        """
        if direction == 'horizontal':
            for i in range(len(word)):
                self.grid[row][col + i] = word[i]
        else:
            for i in range(len(word)):
                self.grid[row + i][col] = word[i]

    def place_words(self, words):
        """
        Attempt to place a list of words into the grid.

        Parameters:
            words (list[str]): Words to place in the puzzle.
        """
        for word in words:
            word = word.upper()
            placed = False

            for _ in range(100):
                direction = random.choice(['horizontal', 'vertical'])
                row = random.randint(0, self.rows - 1)
                col = random.randint(0, self.columns - 1)

                if self._can_place(word, row, col, direction):
                    self._place(word, row, col, direction)
                    self.words.append(word)
                    placed = True
                    break

            if not placed:
                print(f"Could not place {word}")

    def fill_random(self):
        """
        Fill all empty cells in the grid with random uppercase letters.
        """
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range(self.rows):
            for c in range(self.columns):
                if self.grid[r][c] == '':
                    self.grid[r][c] = random.choice(alphabet)
       

    def display(self):
        """
        Print the grid to the console in a readable format.
        """
        for row in self.grid:
            for letter in row:
                print(letter, end=" ")
            print()




def input_validation(guess, word_list, guessed_words):
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

    normalized_guess = guess.strip().lower()

    if normalized_guess in guessed_words:
        return False, f"You already guessed' '{normalized_guess}'. Try a new word."

    if normalized_guess not in word_list:
        return False, f"'{normalized_guess}' is not a valid word for this round."

    guessed_words.add(normalized_guess)

    return True, f"Good job! '{normalized_guess}' is a valid word."

class GameState:
    
    """
    Represents the state of a Word Hunt game.
    Args: 
        topic(str): The chosen topic for the game.
        difficulty(str): The chosen difficulty level for the game.
        guessed_words(set): A set of words that the player has already guessed.
    Attributes:

        score(int): The player's current score.
        """
    def __init__(self, topic=None, difficulty=None, word=None, score=0):
        self.player_name = None  # game name to be added later
        self.topic = topic
        self.difficulty = difficulty
        self.word = word
        self.guessed_words = set()
        self.score = score

    def set_player_name(self):
        """
        Prompts the user to enter their name and sets it as the player_name attribute.

        Returns:
            str: th= game's name
        """
        while True:
            name = input("Enter your name: ").strip()
            if name:
                self.player_name = name
                print(f"Welcome, {self.player_name}!")
                return self.player_name
            else:
                print("Name cannot be empty. Please enter a valid name.")

    def Topic(self):
        """
        Tells user to pick a topic for the game, and the topic and difficulty
        are intertwined. so sports is easy, animals is medium and plants is hard.
        Args:
            topic (str): The chosen topic for the game.
        Raises:
            ValueError: If the topic is not one of the valid options.
        Returns:
            topic (str): The chosen topic for the game.
        """

        choice = input(
            "Choose a topic \n 1. Sports: Easy \n 2. Animals: Medium \n 3. Plants: Hard\n").lower().strip()

        if choice == "1":
            topic = "sports"
        elif choice == "2":
            topic = "animals"
        elif choice == "3":
            topic = "plants"
        else:
            if topic not in topicdict:
                raise ValueError(
                    "Invalid topic. Please choose from plants, animals, or sports.")
        self.topic = topic
        print(f"You have chosen the topic: {topic}")

        # going to do the random subset of words for the topic that they pick
        # number of words depending on topic
        num_words = {"plants": 5, "animals": 4, "sports": 3}
        self.word = random.sample(topicdict[topic], min(
            num_words[topic], len(topicdict[topic])))
        return topic

    def countdown(self):
        """
        This function acts as both a countdown before the User can input their 
        guess, and to count how long it takes them to answer the theme word 
        hunt. depending on time this will be affect their total score. 

    Args:
        choice (str): choice for the theme(difficulty) they choose in the game

    Returns:
        bonus (INT): returns the score with bonus (depending on difficulty).
        time (INT): returns the time in secconds, how long it took to answer. 
    """
        while True:
            print("Are You Ready? (Y/N)")
            answer = input(">> ")
            if answer.upper() == "Y":
                break
        start = True

        if start is True:
            count_down = 3
            while count_down > 0:
                print(f"Count down from {count_down}")
                time.sleep(1)
                count_down -= 1
            print("Start!")

def timer(self, difficulty):
    """
        This function acts as both a countdown before the User can input their 
        guess, and to count how long it takes them to answer the theme word 
        hunt. depending on time this will be affect their total score. 

    Args:
        choice (str): choice for the theme(difficulty) they choose in the game

    Returns:
        bonus (INT): returns the score with bonus (depending on difficulty).
        time (INT): returns the time in secconds, how long it took to answer. 
    """
    while True:
        print("Are You Ready? (Y/N)")
        answer = input(">> ")
        if answer.upper() == "Y":
            break
    start = True

    if start is True:
        count_down = 3
        while count_down > 0:
            print(f"Count down from {count_down}")
            time.sleep(1)
            count_down -= 1
        print("Start!")


def input_validation(guess, word_list, guessed_words):
    """
    Validates a players guess in a word hunt game 

    Parameters:
        guess(str): The word guessed by the user 
        word_list(set): The set of valid words for the current topic ot round.
        guessed_words(set): The set of words th= game has already guessed 

    Returns: 
        tuple: (is_valid, message)[].
        is_valid (bool): True is the guess is valid and new, False otherwise. 
        message(str): Explanation of the result
    """

    if not isinstance(guess, str) or not guess.strip():
        return False, "Invalid input. Please enter a word,"

    normalized_guess = guess.strip().lower()

    if normalized_guess in guessed_words:
        return False, f"You already guessed' '{normalized_guess}'. Try a new word."

    if normalized_guess not in word_list:
        return False, f"'{normalized_guess}' is not a valid word for this round."

    guessed_words.add(normalized_guess)

    return True, f"Good job! '{normalized_guess}' is a valid word."


def timer():
    """
        This function acts as both a countdown before the User can input their 
        guess, and to count how long it takes them to answer the theme word 
        hunt. depending on time this will be affect their total score. 

    Args:
        choice (str): choice for the theme(difficulty) they choose in the game

    Returns:
        bonus (INT): returns the score with bonus (depending on difficulty).
        time (INT): returns the time in secconds, how long it took to answer. 
    """

    time_start = time.time()
    while True:
        if input_user.upper() == "DONE":
            break
    time_end = time.time()
    total_time = time_end - time_start


def main():

    game = GameState()
    name = game.set_player_name()
    topic = game.Topic()
    game.countdown()
    display = Grid(rows=10, columns=10)
    display.place_words(game.word)
    display.fill_random()
    display.display()
    
    game_list = set(w.lower() for w in game.word)

    input_list = set()
    
    while True:
        if game_list != input_list:
            guess = input("Guess: ").strip().lower()
            
        if guess == "done":
            print ("Well Done")
            break 
    
    is_valid, message = input_validation (guess, game_list, input_list)
    print(message)
    
    if is_valid: 
        input_list.add(guess)
    

if __name__ == "__main__":
    main()
