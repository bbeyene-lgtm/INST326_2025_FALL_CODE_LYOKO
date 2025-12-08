import random
from collections import Counter
import sys
import argparse
import time



#example topic not real
plants = ["trees", "flowers", "shrubs", "herbs","tulips","roses","daisies","bushes"
          "ferns","mosses","cacti","vines","grasses","palms","sunflowers","lilies",
          "orchids","daffodils","irises","marigolds","lavender", "jasmine","peonies",
          "begonias","chrysanthemums","hydrangeas","azaleas","camellias","gardenias","grasses",
          "bamboo","succulents","aloe vera","sage","thyme","rosemary","basil","mint","oregano",
          "cilantro","parsley","dill","fennel","chives","lemongrass","tarragon","bay leaves",
          "coriander","lavender","echinacea","ginseng","chamomile","valerian"]

animals = ["dog", "cat", "elephant", "tiger","lion","bear","wolf","fox",
           "giraffe","zebra","kangaroo","panda","monkey","rabbit","deer",
           "squirrel","hedgehog","otter","raccoon","badger","beaver", "moose"
           ,"buffalo","bison","antelope","cheetah","leopard","hyena","jaguar",
           "cougar","lynx","bobcat","caracal","ocelot","tapir","armadillo",
           "sloth","anteater","porcupine","wombat","echidna","platypus","dingo",\
            "quokka","quoll","numbat","bandicoot","monkeypox","lemur","tarsier",
           "marmoset","capuchin","howler","spider monkey","sakin","uakari",
           "colobus","langur","gibbon","siamang","orangutan","chimpanze","lizard",
            "gecko","iguana","chameleon","anole","skink","monitor","python",]

sports = ["soccer", "basketball", "baseball", "tennis","golf","cricket",
          "rugby","hockey","volleyball","badminton","table tennis","swimming",
          "cycling","running","boxing","wrestling","skiing","snowboarding", "skateboarding",
          "surfing","sailing","rowing","fishing","archery","fencing","gymnastics",
          "weightlifting","yoga","pilates","aerobics","dance","cheerleading",
          "karate","judo","taekwondo","kickboxing","mixed martial arts","triathlon",
          "marathon","ultramarathon","hiking","climbing","caving","orienteering",
          "parkour","bouldering","curling","luge","skeleton","bobsledding",
          "handball","water polo","synchronized swimming","diving","triathlon",]

topicdict = {
    "plants": plants,
    "animals": animals,
    "sports": sports,}


alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#the lcd function will be worked out, this is just a draft of something that I 
# think could work, but might be scrapped later on if we find a better way to do it

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
    def __init__(self, topic, difficulty, word, score = 0):
        self.topic = topic
        self.difficulty = difficulty
        self.word = word
        self.guessed_words = set()
        self.score = score
        
    def Topic(self,topic):
        """
        Tells user to pick a topic for the game.
        Args:
            topic (str): The chosen topic for the game.
        """
        topic = input("Choose a topic (plants, animals, sports): ")
        if topic not in topicdict:
            raise ValueError("Invalid topic. Please choose from plants, animals, or sports.")
        self.topic = topic
        print(f"You have chosen the topic: {topic}")
        return topic
        

def LCD():
    """
    Generates a Letter Common Denominator (LCD) set for a Word Hunt puzzle.
    
    The LCD algorithm chooses letters based on frequency within a topic-
    specific word list. This ensures that:
        - Easy mode → high-frequency letters → easier puzzle
        - Hard mode → low-frequency letters → less common letters → harder puzzle
    
    The algorithm also allows words to be found reversed.
    
    Returns:
        dict: Contains selected letters, topic, difficulty, and playable words.
    """
    
    print("Welcome to word hunt!")
    print("Choose a topic:\n1. Plants\n2. Animals\n3. Sports")
    choice = input("> ")

    topic_map = {"1": "plants", "2": "animals", "3": "sports"}
    topic = topic_map.get(choice, "plants")
    words = topicdict[topic]

    # Ask for difficulty selection
    print("\nDifficulty Levels:\n1. Easy\n2. Medium\n3. Hard")
    difficulty = input("Pick Difficulty Level (1-3):")

 
    letter_freq = {}
    for word in words:
        for letter in word.lower():
            if letter.isalpha():
                letter_freq[letter] = letter_freq.get(letter, 0) + 1

    
    sorted_letters = sorted(letter_freq.keys(), key=lambda x: letter_freq[x], reverse=True)

   
    
    if difficulty == "1":       # Easy: most common letters
        pool = sorted_letters[:12]
    elif difficulty == "3":     # Hard: least common letters
        pool = sorted_letters[-12:]
    else:                       # Medium: middle range
        mid = len(sorted_letters) // 2
        pool = sorted_letters[mid-6 : mid+6]

    return {
        "topic": topic,
        "difficulty": difficulty,
        "letters": selected_letters,
        "words": playable
    }

def input_validation (guess, word_list, guessed_words):
    
    """
    Validates a players guess in a word hunt game 
gt
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
        return False, f"You already guessed' '{normalized_guess}'. Try a new word."
    
    if normalized_guess not in word_list: 
        return False, f"'{normalized_guess}' is not a valid word for this round."
    
    guessed_words.add(normalized_guess)
    
    return True, f"Good job! '{normalized_guess}' is a valid word."  


class Grid:
    def __init__(self,rows=10, columns=10):
        self.rows=rows
        self.columns=columns
        self.grid= [['' for _ in range(columns)] for _ in range(rows)]
        self.words= []
        
    
    def place_words(self, words):
        for word in words:
            word = word.upper()
            placed = False
            for _ in range(100):
                direction = random.choice(['horizontal', 'vertical'])
                row = random.randint(0, self.rows - 1)
                col = random.randint(0, self.cols - 1)
                if self._can_place(word, row, col, direction):
                    self._place(word, row, col, direction)
                    self.words.append(word)
                    placed = True
                    break
            if not placed:
                print(f"Could not place {word}")
    def _can_place(self, word, row, col, direction):
        if direction == 'horizontal':
            if col + len(word) > self.cols: return False
            return all(self.grid[row][col+i] in ('', word[i]) for i in range(len(word)))
        if direction == 'vertical':
            if row + len(word) > self.rows: return False
            return all(self.grid[row+i][col] in ('', word[i]) for i in range(len(word)))
        return False

    def _place(self, word, row, col, direction):
        if direction == 'horizontal':
            for i in range(len(word)):
                self.grid[row][col+i] = word[i]
        else:
            for i in range(len(word)):
                self.grid[row+i][col] = word[i]

    def fill_random(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == '':
                    self.grid[r][c] = random.choice(alphabet)

    def display(self):
        for row in self.grid:
            for letter in row:
                print(letter, end=" ")


def timer(choice):
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
    gamepick = ""
    while count_down > 0:
        print(f"Count down from {count_down - 1}")
        time.sleep(1)
        count_down -= 1
    if count_down == 1:
        print("START!")
        time.sleep(1)

    if count_down == (0) and gamepick == choice:

        time_start = time.time()
        input_user = input(guess)
        time_end = time.time()
    
        total_time = time_end - time_start
    
        if choice == 1:
            bonus_1 = total_score
            return (bonus_1, print(total_time))

        elif choice == 2:
            bonus_2 = total_score * 1.25
            return (bonus_2, print(total_time))

        else:
            bonus_3 = total_score * 1.50
            return (bonus_3, print(total_time))