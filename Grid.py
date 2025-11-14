import random
from collections import Counter

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

        
                

                
        
                    