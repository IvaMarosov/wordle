from src.game_logic import WordleGame
from src.letter_state import LetterState
from src.words import get_list_of_words
from colorama import Fore
import random


def _is_valid_guess(word: str, word_length: int) -> bool:
    """Check if the guessed word has the expected length."""
    return len(word) == word_length


def display_results(wordle: WordleGame) -> None:
    print("\nYour results so far...")
    print(f"You have {wordle.remaining_guesses} guesses left.\n")

    lines = []

    for word in wordle.guesses:
        result = wordle.resolve_guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_guesses):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_border(lines)


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

    return " ".join(result_with_color)


def draw_border(lines: list[str], box_size: int = 9, padding: int = 1):
    content_length = box_size + padding * 2

    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * padding

    print(top_border)
    [print("│" + space + line + space + "│") for line in lines]
    print(bottom_border)


def main():
    print("Hello from wordle!")

    words = get_list_of_words()
    secret_word = random.choice(words).upper()

    game = WordleGame()

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
        print(f"The correct word was: {secret_word}!")


if __name__ == "__main__":
    main()
