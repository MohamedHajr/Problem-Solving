def is_pangram(sentence):
    sentenceSet = set(sentence.lower)
    alpha = [ch for ch in sentenceSet if ord(ch) in range(ord('a'), ord('z')+1)]
    if len(alpha) == 26 : return True
    else : return False
