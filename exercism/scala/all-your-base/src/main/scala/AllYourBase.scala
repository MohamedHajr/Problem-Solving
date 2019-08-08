import scala.annotation.tailrec
object AllYourBase {
  def isValid(base: Int, target: Int, digits: List[Int]): Boolean  =
    base <= 1 || target <= 1 || digits.isEmpty || digits.exists(n => n >= base || n < 0)
  
  def convertToBase10(number: List[Int], base: Int): Int = {
    if( base == 10) {
      number.mkString.toInt
    } else 
      number
        .zipWithIndex
        .map{ case (x, index) => (math.pow(base, index) * x).toInt }
        .sum
  }

  @tailrec def convertFromBase10(number: Int, base: Int, acc: List[Int]): List[Int] =  number match {
    case _ if number <= 0 => acc 
    case x => convertFromBase10(number / base, base, (x % base) :: acc)
  }

  def rebase(base: Int, number: List[Int], targetBase: Int): Option[List[Int]] = {
    if(isValid(base, targetBase, number))
      Some(convertFromBase10(convertToBase10(number, base), targetBase, List.empty))  
    else
      None 
  } 
}
