"""The wordle is out!"""

__author__ = "730437270"

def contains_char(searched_word: str, searched_char: str) -> bool:
    """Extracts single character in searched word."""
    assert len(searched_char) == 1
    index_test: bool = False
    counter: int = 0 
    while  counter < len(searched_word):
        if searched_word[counter] == searched_char[0]:
           index_test = True 
           return index_test
        counter += 1
        
    
    return index_test

def emojified(guess: str, secret: str) -> str:
    """Return string of emoji whose color codifies."""
    assert len(guess) == len(secret)
    index_test: bool = False
    counter: int = 0
    res_emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while counter < len(secret):
        if secret[counter] == guess[counter]:
            res_emoji += (GREEN_BOX)

    else:
        index_test = False
        if contains_char(secret, guess[counter]):
            index_test = True
        if index_test:
            res_emoji += (YELLOW_BOX)
        else:
            res_emoji += (WHITE_BOX)
    counter += 1 
    return res_emoji 