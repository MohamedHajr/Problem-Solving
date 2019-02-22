#V1
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

print('Is Permutation -> ',isPermutation('aaa', 'csc'))
print('Is Permutation -> ',isPermutation('abc', 'cba'))
print('Is Permutation -> ',isPermutation('as', 'cba'))