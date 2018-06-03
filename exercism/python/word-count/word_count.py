import re

def word_count(phrase):
    cleanPhrase = re.compile("(\\n|\\t|_|,|' | ')").sub(' ', phrase.lower())
    words = re.compile("[a-z\d']+").findall(cleanPhrase)
    return { word: words.count(word) for word in words }
