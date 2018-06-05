from random import shuffle

def is_balanced(list):

    counter = 0
    for element in list:
        if element == "[":
            counter += 1
        else:
            if counter == 0:
                return False
            counter -= 1
    return True


def generate_string(n):
    brackets = ["[" for i in range(n)] + ["]" for i in range(n)]
    shuffle(brackets)
    return brackets


if __name__ == "__main__":
    string = generate_string(5)

    if is_balanced(string):
        print(''.join(string), "\t", "OK!")
    else:
        print(''.join(string), "\t", "Not OK!")