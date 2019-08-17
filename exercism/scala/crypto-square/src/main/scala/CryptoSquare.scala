import scala.annotation.tailrec
object CryptoSquare {

  def normalize(text: String): String = text.toLowerCase.filter(_.isLetterOrDigit)

  @tailrec def findMultiples(n: Int, acc: Int): (Int, Int) = {
    val squareOfN = math.sqrt(n).ceil.toInt
    val multiple = (2 to squareOfN) find { x => n % x == 0 &&  n / x - x <= 1 }
    multiple match {
      case None => findMultiples(n + 1, acc + 1)
      case Some(x) => (n / x, acc)
    }
  }

  @tailrec def transpose(words: List[String], result: List[String]): List[String] = words.head.isEmpty match {
    case true => result
    case _ => { 
      transpose(words map (_.tail), (words map (_.head) mkString) :: result)
    }
  }
    
  def ciphertext(text: String): String = {
    val normalized = normalize(text)
    if(normalized.size <= 1) 
      normalized
    else {
      val (row, margin) = findMultiples(normalized.size, 0)
      val textAfterPadding = normalized ++ (" " * margin)
      val transposed = transpose(textAfterPadding.grouped(row).toList, List.empty)
      transposed.reverse.mkString(" ") 
    }
  } 
}
