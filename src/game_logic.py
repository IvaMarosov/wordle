

class WordleGame:
    MAX_GUESSES = 6
    WORD_LENGTH = 5

    def __init__(self, secret_word: str):
        self.secret_word = secret_word
        self.guesses = []

    @property
    def is_solved(self) -> bool:
        """Game is solved if the latest guess is equal to the secret word."""
        return self.guesses[-1] == self.secret_word

    @property
    def can_guess(self) -> bool:
        """The player has another guess if he does not run out of guesses and
        his last guess was not correct."""

        return not self.is_solved and len(self.guesses) < self.MAX_GUESSES
