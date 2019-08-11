object AtbashCipher {
  def rotate(c: Char): Char = (122 - (c.asDigit - 10)).toChar 
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
