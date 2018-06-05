from random import randint
from copy import deepcopy


words = ["snake", "first", "tiger", "shops", "snoop", "spoon",
         "macho", "goals", "purse", "punch", "dairy", "dirty",
         "treat", "after", "affix"]


def get_word():
    index = randint(0, len(words)-1)
    return words[index]


def get_clue(word, guess):
    print(word)
    if len(guess) != 5:
        return "Try words with 5 letters only."

    clue = ""
    i = 0
    word_temp = set(deepcopy(word))
    while i < len(word):
        if word[i] == guess[i]:
            clue += "[" + guess[i] + "]"
            word_temp.remove(word[i])
        elif guess[i] in word_temp:
            clue += "(" + guess[i] + ")"
        else:
            clue += guess[i]

        i += 1

    return clue

def start_game():

    word = get_word()

    print("Let's Begin!")

    while True:
        guess = (input("Take a guess: "))

        if guess == word:
            print("Well Done.")
            return
        else:
            print("Clue: ", get_clue(word, guess))
            print("Nope!")


if __name__ == "__main__":
    start_game()