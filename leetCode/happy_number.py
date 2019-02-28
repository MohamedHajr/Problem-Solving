from math import pow


def isHappy(n, trials=set()):
    if n == 1:
        return True
    n = sum([int(i) ** 2 for i in str(n)])
    if n in trials:
        return False
    trials.add(n)
    return isHappy(n, trials)


print(isHappy(7))
