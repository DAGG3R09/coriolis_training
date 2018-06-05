from random import randint


def start_game():
    name = input("Enter Name: ")

    print ("Well, " + name + ", I am thinking of a number between 1 and 20.")

    guess_count = 0
    number = randint(1, 20)
    while True:
        guess = int(input("Take a guess: "))
        guess_count += 1
        if guess == number:
            print("Well Done. You got that right in ", str(guess_count), " guesses!")
            return
        elif guess < number:
            print("Go HIGHER!")
        else:
            print("Go LOWER!")


if __name__ == "__main__":
    start_game()