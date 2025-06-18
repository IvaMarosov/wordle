from src.game_logic import WordleGame
from src.letter_state import LetterState
from colorama import Fore


def _is_valid_guess(word: str, word_length: int) -> bool:
    """Check if the guessed word has the expected length."""
    return len(word) == word_length


def display_results(wordle: WordleGame):
    for word in wordle.guesses:
        result = wordle.resolve_guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)


def convert_result_to_color(result: list[LetterState]) -> str:
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return "".join(result_with_color)


def main():
    print("Hello from wordle!")
    game = WordleGame("APPLE")

    while game.can_guess:
        x = input("Enter your guess: ")
        x = x.upper()
        if not _is_valid_guess(x, game.WORD_LENGTH):
            print(
                Fore.RED
                + f"Word must be {game.WORD_LENGTH} letters long.."
                + Fore.RESET
            )
            continue

        game.add_guess(x)
        display_results(game)

    if game.is_solved:
        print("You solved the puzzle!")
    else:
        print("You run out of guesses!")


if __name__ == "__main__":
    main()
