from src.game_logic import WordleGame


def main():
    print("Hello from wordle!")
    game = WordleGame("APPLE")

    while game.can_guess:
        x = input("Enter your guess: ")
        game.add_guess(x)
        result = game.resolve_guess(x)
        print(*result, sep="\n")

    if game.is_solved:
        print("You solved the puzzle!")
    else:
        print("You run out of guesses!")


if __name__ == "__main__":
    main()
