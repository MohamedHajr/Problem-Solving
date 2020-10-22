def is_isogram(word):
    cleanWord = word.lower().replace("-", "").replace(" ", "")
    return len(cleanWord) == len(set(cleanWord))

def is_isogram_v2(word):
  clean_word = word.lower()
  holder = []

  for letter in clean_word :
      if letter in holder and letter != " " and letter != '-' : return False
      holder.append(letter)

  return True

