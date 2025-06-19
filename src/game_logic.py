from src.letter_state import LetterState, ResolvedGuess


class WordleGame:
    MAX_GUESSES = 6
    WORD_LENGTH = 5

    def __init__(self, secret_word: str):
        self.secret_word = secret_word
        self.resolved_guesses = []

    @property
    def remaining_guesses(self) -> int:
        """How many guesses has the player till the game is over."""
        return self.MAX_GUESSES - len(self.resolved_guesses)

    @property
    def is_solved(self) -> bool:
        """Game is solved if the latest guess is equal to the secret word."""
        return (
            len(self.resolved_guesses) > 0
            and self.resolved_guesses[-1].guess == self.secret_word
        )

    @property
    def can_guess(self) -> bool:
        """The player has another guess if he does not run out of guesses and
        his last guess was not correct.
        """
        return not self.is_solved and self.remaining_guesses > 0

    def resolve_guess(self, word: str) -> list[LetterState]:
        """For every character in given guessed word, check that:
        - this character is present in the secret word
        - this character is in the correct position in the secret word
        """
        result = []

        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in set(self.secret_word)
            letter.is_in_position = character == self.secret_word[i]
            result.append(letter)

        return result

    def add_guess(self, word: str) -> None:
        """Add the latest guess in the list."""
        letter_states = self.resolve_guess(word)
        resolved_guess = ResolvedGuess(word, letter_states)
        self.resolved_guesses.append(resolved_guess)
