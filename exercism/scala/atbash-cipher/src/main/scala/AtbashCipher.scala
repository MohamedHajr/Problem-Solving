object AtbashCipher {
  def rotate(c: Char): Char = ('z' - (c - 'a')).toChar
  def encode(sentence: String): String = sentence
    .toLowerCase
    .filter(_.isLetterOrDigit)
    .map { 
      case c if c.isLetter => rotate(c)
      case notLetter => notLetter
    } 
    .grouped(5)
    .mkString(" ")

  def decode(sentence: String): String = sentence
    .filter(_.isLetterOrDigit)
    .map {
    case c if c.isLetter => rotate(c) 
    case notLetter => notLetter
    }
  
}
