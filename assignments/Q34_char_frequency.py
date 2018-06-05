from sys import argv
from operator import itemgetter


def char_freq_table(filename):
    chars = dict()
    for line in open(filename, "r"):
        for char in line:
            if chars.get(char, None) == None:
                chars[char] = 1
            else:
                chars[char] += 1

    return chars


def print_frequency_table(frequency):
    sorted_x = sorted(frequency.items(), key=itemgetter(0))

    for char, count in sorted_x:
        if char == "\n" :
            print("newline", count)
        else:
            print(char, count)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Please Enter File name.\nExiting..")
        exit(1)

    frequency = char_freq_table(argv[1])

    print_frequency_table(frequency)
