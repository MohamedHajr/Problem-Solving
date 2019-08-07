object ScrabbleScore {
  def score(text: String): Int = {
    val lettersValues = Map(
      'D'-> 2,
      'G'-> 2,
      'B' -> 3, 'C' -> 3, 'M' -> 3,'P' -> 3,
      'F' -> 4, 'H' -> 4, 'V' -> 4, 'W' -> 4, 'Y' -> 4,
      'K' -> 5,  'J' -> 8, 'X' -> 8, 'Q' -> 10, 'Z' -> 10 
    )
    text.foldLeft(0){ (acc, c) => acc + lettersValues.getOrElse(c.toUpper, 1) }
  }
}
