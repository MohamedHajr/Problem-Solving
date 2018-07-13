from string import ascii_lowercase
import functools

# Dictionary representing the morse code chart
MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
         "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]


def uniqueMorseRepresentations(words):
        return len(set(map(lambda word: encrypt(word), words)))


def encrypt(word):
    return functools.reduce(lambda accumlator, letter: accumlator + MORSE[ord(letter) - ord('a')], word, '')
