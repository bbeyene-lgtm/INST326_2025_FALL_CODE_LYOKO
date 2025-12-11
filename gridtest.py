import random

class Grid:
    def __init__(self, rows=10, columns=10):
        self.rows = rows
        self.columns = columns
        self.grid = [['' for _ in range(columns)] for _ in range(rows)]
        self.words = []

    def place_words(self, words):
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

    def _can_place(self, word, row, col, direction):
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
        if direction == 'horizontal':
            for i in range(len(word)):
                self.grid[row][col+i] = word[i]
        else:
            for i in range(len(word)):
                self.grid[row+i][col] = word[i]

    def fill_random(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range(self.rows):
            for c in range(self.columns):
                if self.grid[r][c] == '':
                    self.grid[r][c] = random.choice(alphabet)

    def display(self):
        for row in self.grid:
            for letter in row:
                print(letter, end=" ")
            print()  



if __name__ == "__main__":
    words = ["lion", "tiger", "zebra", "bison"]  # example words
    game_grid = Grid(rows=10, columns=10)
    game_grid.place_words(words)
    game_grid.fill_random()
    game_grid.display()
