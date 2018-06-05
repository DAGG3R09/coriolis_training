from Q17_panlindrome_recognizer import palindrome_recognizer


def palindrome_checker(filename):
    for line in open(filename, "r"):
        print(line.strip(), ": ",palindrome_recognizer(line))


if __name__ == "__main__":
    palindrome_checker("files/palindrome.txt")