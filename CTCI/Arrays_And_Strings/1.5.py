# V1


def isOneEditAway(s1, s2):
    if s1 == s2:
        return True
    if abs(len(s1) - len(s2)) > 1:
        return False
    map = set()
    for char in s1:
        map.add(char)
    for char in s2:
        if char in map:
            map.remove(char)
        else:
            map.add(char)
    print('results -> ', map)
    return True if len(map) <= 2 else False


print('4 real cuz -> ', 'yaahh son' if isOneEditAway('pale', 'bake') else 'Shame son!')
print('4 real cuz -> ', 'yaahh son' if isOneEditAway('pale', 'pal') else 'Shame son!')
