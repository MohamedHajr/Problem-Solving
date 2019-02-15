# V1
def isUnique_v1(s):
    if len(s) == 1:
        return True

    first_char = s[0]
    rest = s[1:]
    if first_char in rest:
        return False
    return isUnique_v1(rest)

# V2


def isUnique_v2(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        val_flag = 1 << val
        if checker & val_flag > 0:
            return False
        checker |= val_flag
    return True

print("Suppose to be True", isUnique_v2('abcdefg'))
print("Suppose to be False", isUnique_v2('adbca'))
