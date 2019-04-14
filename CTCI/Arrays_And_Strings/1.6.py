# V1


def compress(s):
    letter = s[0]
    count = 0
    final = ''
    more_needed = True
    for char in s:
        if letter == char:
            count += 1
            more_needed = True
        else:
            final += f'{letter}{count}'
            letter = char
            count = 1
            more_needed = False
    if more_needed:
        final += f'{letter}{count}'
    return final if len(final) < len(s) else s

# v2


class StringBuilder(object):
    def __init__(self, initial_val):
        self.storage = [initial_val]


    def __iadd__(self, incoming):
        self.storage.append(incoming)
        return self

    def toStr(self):
        return ''.join(self.storage)
        


def compress_v2(s):
    result = StringBuilder('')
    count = 0
    for i, char in enumerate(s):
        count += 1
        if (i+1) >= len(s) or char != s[i+1]:
            result += f'{char}{count}'
            count = 0
    final = result.toStr()
    return final if len(final) < len(s) else s

print('bruhhhh?', 'Hell Yeah' if 'a1b1c1' ==
      compress_v2('abc') else 'Daaaamn son')
print('bruhhhh?', 'Hell Yeah' if 'a2b1c5a3' ==
      compress_v2('aabcccccaaa') else 'Daaaamn son')
