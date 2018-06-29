def detect_anagrams(word, candidates):
    return list (filter( (lambda x : sorted(firstToLower(x)) == sorted(firstToLower(word))), candidates))

firstToLower = lambda s: s[:1].lower() + s[1:] if s else ''