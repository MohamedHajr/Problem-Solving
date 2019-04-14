# V1
def isPermutation(s1, s2):
    tmp = set()
    if not len(s1) == len(s2):
        return False
    for char1, char2 in zip(s1, s2):
        if char1 in tmp:
            tmp.remove(char1)
        else:
            tmp.add(char1)
        if char2 in tmp:
            tmp.remove(char2)
        else:
            tmp.add(char2)
    return True if len(tmp) == 0 else False


# V2
def isPermu(s1, s2):
    if not len(s1) == len(s2):
        return False

    store = 0
    for a, b in zip(s1, s2):
        store += ord(a)
        store -= ord(b)
    return True if store == 0 else False


print('Is Permutation -> ', isPermu('aaa', 'csc'))
print('Is Permutation -> ', isPermu('abc', 'cba'))
print('Is Permutation -> ', isPermu('as', 'cba'))
