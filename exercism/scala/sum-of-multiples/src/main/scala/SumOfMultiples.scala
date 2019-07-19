import scala.annotation.meta.setter
object SumOfMultiples {
  def find_multiples_until(x: Int, limit: Int): List[Int] = 
      (x to limit).filter(_ % x == 0).toList
  def sum(factors: Set[Int], limit: Int): Int = 
    factors.map(find_multiples_until(_, limit)).flatten.sum
}