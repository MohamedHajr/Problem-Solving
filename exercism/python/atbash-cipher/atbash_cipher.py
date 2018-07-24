from string import ascii_lowercase

def encode(plain_text):
    ciphered_text = decode(plain_text)
    return ' '.join(ciphered_text[i:i + 5] for i in range(0, len(ciphered_text), 5))


def decode(ciphered_text):
    stripped_text = ''.join(e.lower() for e in ciphered_text if e.isalnum())
    translation = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
    return stripped_text.translate(translation)
