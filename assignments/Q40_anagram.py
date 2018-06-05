from random import shuffle, randint
from copy import deepcopy

colours = ["red","brown", "black", "green", "yellow", "magenta"]

def get_word():
    index = randint(0, len(colours)-1)
    return colours[index]


def start_game():

    word = get_word()
    original = deepcopy(word)

    word = list(word)
    shuffle(word)
    anagram = ''.join(word)

    print("Anagram of word:", anagram)

    while True:
        guess = (input("Take a guess: "))

        if guess == original:
            print("Well Done.")
            return
        else:
            print("Nope!")


if __name__ == "__main__":
    start_game()