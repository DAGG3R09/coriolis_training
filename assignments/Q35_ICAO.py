from os import system
from time import sleep
from gtts import gTTS

key = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}


def generate_audio(word):
    tts = gTTS(text=word, lang="en")
    tts.save("word.mp3")


def translate(word):
    sent = []
    for char in word:
        sent.append(key[char])

    return sent


def speak_ICAO(string, ICAO_delay, word_delay):
    string = string.lower()
    print(string)
    for word in string.strip().split():
        sentence = translate(word)

        for word in sentence:
            generate_audio(word)
            system("mpg321 word.mp3")
            sleep(ICAO_delay)

        sleep(word_delay)

    system("rm word.mp3")


if __name__ == "__main__":
    speak_ICAO("Sufiyan Parkar", 0.2, 1.0)