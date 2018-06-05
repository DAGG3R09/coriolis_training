
sentence_enders = {'.', '!', '?'}
titles = {"Mr.", "Mrs.", "Dr."}

def sentence_splitter(text):

    line = ""
    lines = []
    for i, char in enumerate(text):
        if char in sentence_enders:
            if (i+1) < len(text) and (i+2) < len(text):
                if (
                        text[i+1] == ' '
                        and text[i+2].isupper()
                        and text[i-2: i+1]
                        and text[i-3: i+1]
                ):
                    line += char
                    lines.append(line.strip())
                    line = ""
                    continue
        line += char

    lines.append(line.strip())
    return lines


if __name__ == "__main__":

    l = open("files/sentence_splitter.txt", "r").readlines()[0]
    print(l)
    # print(sentence_splitter(l.strip()))

    output = sentence_splitter(l.strip())
    fh = open("files/output.txt", "w")

    for l in output:
        fh.write(l+"\n")