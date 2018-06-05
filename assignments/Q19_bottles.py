import re

verses = """99 bottles of beer on the wall, 99 bottles of beer.
            Take one down, pass it around, 98 bottles of beer on the wall.
            """


def sing(verse):
    flag = 0

    while True:
        numbers = re.findall('\d+', verse)
        numbers.sort()
        for num in numbers:
            verse = re.sub(num, str(int(num)-1), verse)

            if (int(num)-1) == 0:
                flag = 1

        print(verse)
        if flag:
            return


if __name__ == "__main__":
    sing(verses)