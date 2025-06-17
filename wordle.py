from src.game_logic import WordleGame


def _is_valid_guess(word: str, word_length: int) -> bool:
    """Check if the guessed word has the expected length."""
    return len(word) == word_length


def main():
    print("Hello from wordle!")
    game = WordleGame("APPLE")

    while game.can_guess:
        x = input("Enter your guess: ")
        x = x.upper()
        if not _is_valid_guess(x, game.WORD_LENGTH):
            print(f"Word must be {game.WORD_LENGTH} letters long..")
            continue

        game.add_guess(x)
        result = game.resolve_guess(x)
        print(*result, sep="\n")

    if game.is_solved:
        print("You solved the puzzle!")
    else:
        print("You run out of guesses!")


if __name__ == "__main__":
    main()
