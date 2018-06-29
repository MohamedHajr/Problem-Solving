def rotate(text, key):
    return cipher(text = text, key = key)

def cipher(*, text, result = '', key):
    if text == '': return result

    if text[0].isalpha() and text[0].isupper() :
        print(chr((ord(text[0]) + key - 65) % 26 + 65))
        return cipher( text = text[1:], result = result + chr((ord(text[0]) + key - 65) % 26 + 65), key = key)

    elif text[0].isalpha() :
        return cipher( text = text[1:], result = result + chr((ord(text[0]) + key - 97) % 26 + 97), key = key)

    else :
        return cipher( text = text[1:], result = result + text[0], key = key)

### salahmar elagant soultion
# import re
# import string

# def replace_by_next_letter(key):
#     def replace_char(char):
#        characters = string.ascii_uppercase if char.group().isupper() else string.ascii_lowercase
#        return characters[(characters.index(char.group())+key)%26]
#     return replace_char

# def rotate(text, key):
#     if key not in range(0,27):
#         raise ValueError("Key must be between 0 and 26")
#     else:
#        text = re.sub(r'[a-zA-Z]', replace_by_next_letter(key), text)
#        return text