object Diamond {
  def spaces(n: Int): String = " " * n
  def createRow(in : ((Char, Int), Int)): String = in._1 match {
    case ('A', sides) => s"${spaces(sides)}A${spaces(sides)}"
    case (c, sides)   => s"${spaces(sides)}${c}${spaces(in._2)}${c}${spaces(sides)}"
  }

  def createUpper(char: Char): List[String] = {
    val chars = 'A' to char
    val spaces = chars.size - 1 to 0 by -1
    chars zip spaces zip spaces.reverse map createRow toList
  }

  def rows(char: Char): List[String] = {
    createUpper(char) ::: createUpper(char).reverse.drop(1)
  }
}
