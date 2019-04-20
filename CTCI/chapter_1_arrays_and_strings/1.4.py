# V1

def isPermutationPalindorme(s):
    checker = set()
    stripped = s.strip().lower()
    for char in stripped:
        if char in checker:
            checker.remove(char)
        else:
            checker.add(char)
    length = len(checker)
    if length % 2 == 0:
        return True if length == 0 else False
    else:
        return True if length == 1 else False

#V2

def isPP(s):
    checker = 0
    stripped = s.replace(" ", "").lower()
    for char in stripped:
        val =  1 << ord(char) - ord('a')
        checker ^= val
    return True if checker % 2 == 0 else False
    
 

print('4 real cuz ? -> ',
      'yeah son' if isPP('a Santa at Nasa') else 'Shame')
print('4 real cuz ? -> ',
      'yeah son' if isPP('a Santa at Nas') else 'Shame')