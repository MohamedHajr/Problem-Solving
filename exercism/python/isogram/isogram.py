def is_isogram(word):
  clean_word = word.lower()
  holder = []

  for letter in clean_word :
      if letter in holder and letter != " " and letter != '-' : return False
      holder.append(letter)

  return True

