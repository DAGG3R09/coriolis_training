
def reverse_string(string):
    reversed_string = ""
    for s in string:
        reversed_string = s + reversed_string
    return reversed_string


if __name__ == "__main__":
    string = "Reverse this string"
    print(reverse_string(string))