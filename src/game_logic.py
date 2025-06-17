

class WordleGame:
    MAX_GUESSES = 6
    WORD_LENGTH = 5

    def __init__(self, secret_word: str):
        self.secret_word = secret_word
        self.guesses = []

    @property
    def is_solved(self):
        """Game is solved if the latest guess is equal to the secret word."""
        return self.guesses[-1] == self.secret_word



