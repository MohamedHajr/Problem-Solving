def is_pangram(sentence):
    sentence = sentence.lower()
    sentence = set(sentence)
    alpha = [ch for ch in sentence if ord(ch) in range(ord('a'), ord('z')+1)] 
    if len(alpha) == 26 : return True
    else : return False
