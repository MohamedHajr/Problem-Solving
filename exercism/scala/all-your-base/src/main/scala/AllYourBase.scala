import scala.annotation.tailrec
object AllYourBase {
  def isValid(base: Int, target: Int, digits: List[Int]): Option[List[Int]] = {
    val isValid = base <= 1 || target <= 1 || digits.isEmpty || digits.exists(n => n >= base || n < 0)
    
    if(isValid) Option(digits)
    else None
  }
   
  def baseToDecimal(number: List[Int], base: Int): Int = {
    if( base == 10) {
      number.mkString.toInt
    } else  {
      def product(in :(Int, Int)): Int = in._1 * in._2
      val init = math.pow(base, number.size - 1).toInt
      Stream.iterate(init)(_ / base).zip(number).map(product).sum
    }
  }

  def decimalToBase(number: Int, base: Int): List[Int] =  
    Stream.iterate(number)(_ / base).takeWhile(_ > 0).map(_ % base).reverse.toList

  def rebase(base: Int, number: List[Int], targetBase: Int): Option[List[Int]] = 
    isValid(base, targetBase, number).map { digits => 
      decimalToBase(baseToDecimal(number, base), targetBase)
    }
}
