from dataclasses import dataclass


@dataclass
class LetterState:
    character: str = ""
    is_in_word: bool = False
    is_in_position: bool = False


@dataclass
class ResolvedGuess:
    guess: str
    letters: list[LetterState]
