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
    
    normalized_guess = guess.strip().lower()
    
    if normalized_guess in guessed_words: 
        return False, f"You already guessed' '{normalized_guess}'. Try a new word."
    
    if normalized_guess not in word_list: 
        return False, f"'{normalized_guess}' is not a valid word for this round."
    
    guessed_words.add(normalized_guess)
    
    return True, f"Good job! '{normalized_guess}' is a valid word."  


# counldn't figure out how to do it without just using one funtion (will be class)
def grid_gen(words, rows=10, columns=10):
    def empty_grid(rows, columns):
        return [['' for _ in range(columns)] for _ in range(rows)]

    def word_placed(grid, word, row, col, direction):
        if direction == 'horizontal':
            if col + len(word) > columns:
                return False
            for i in range(len(word)):
                if grid[row][col + i] not in ('', word[i]):
                    return False
            return True
        elif direction == 'vertical':
            if row + len(word) > rows:
                return False
            for i in range(len(word)):
                if grid[row + i][col] not in ('', word[i]):
                    return False
            return True
        return False

    def place_word(grid, word, row, col, direction):
        if direction == 'horizontal':
            for i in range(len(word)):
                grid[row][col + i] = word[i]
        elif direction == 'vertical':
            for i in range(len(word)):
                grid[row + i][col] = word[i]

    def get_letters(words):
        letters = [letter.upper() for word in words for letter in word]
        return Counter(letters)

    def weighted_random_letter(freq_counter):
        pool = [letter for letter, count in freq_counter.items() for _ in range(count)]
        return random.choice(pool)

    def fill_remaining_cells(grid, freq_counter):
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '':
                    grid[r][c] = weighted_random_letter(freq_counter)

    grid = empty_grid(rows, columns)
    freq_counter = get_letters(words)

    for word in words:
        word = word.upper()
        placed = False
        for _ in range(100):
            direction = random.choice(['horizontal', 'vertical'])
            row = random.randint(0, rows - 1)
            col = random.randint(0, columns - 1)
            if word_placed(grid, word, row, col, direction):
                place_word(grid, word, row, col, direction)
                placed = True
                break
        if not placed:
            print(f"Unable to place the word '{word}', try again.")

    fill_remaining_cells(grid, freq_counter)
    return grid



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
        topic = [x for x in topicdict if x == topic]
        print(f"You have chosen the topic: {topic}")
        return topic
    def Difficulty(self):
        """
        Tells user to pick a difficulty for the game.
        Args:
            difficulty (str): The chosen difficulty level for the game.
        """
        difficulty = input("Choose a difficulty (easy, medium, hard): ")
        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError("Invalid difficulty. Please choose from easy, medium, or hard.")
        self.difficulty = difficulty
        print(f"You have chosen the difficulty: {difficulty}")
        return difficulty
    
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
        input_user = input("Guess")
        time_end = time.time()
        
        total_score = len(input_user) * 10
    
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
    

