
def number_file(filename):
    """
        Creates a file with name current_filename_n.txt in files folder
    """

    fh = open(filename[:-4]+"_n.txt", "w+")
    for line_no, line in enumerate(open(filename, "r"), 1):
        l = str(line_no) + ": " + line
        fh.write(l)

    fh.close()


if __name__ == "__main__":
    number_file("files/palindrome.txt")
