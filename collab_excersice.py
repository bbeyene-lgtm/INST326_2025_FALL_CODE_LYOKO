print("One Piece is the best anime ever!") #Aggrey
print("Aric is a jerk (Joking, spare me)") #Lizandro 
print("I love cats") #Johana
print("lets skip this exam!!") #Beimnet

import random
from collections import Counter
import sys
import argparse



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

    # Choose 8 letters for the puzzle
    selected_letters = random.sample(pool, 8)

    print(f"\nYour topic: {topic.upper()}")
    print("Your letters:", " ".join(selected_letters).upper())

    playable = []
    for w in words:
        forward = all(letter in selected_letters for letter in w)
        backward = all(letter in selected_letters for letter in w[::-1])

        if forward or backward:
            playable.append(w)

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

        
                

                
        
                    