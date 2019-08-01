import scala.annotation.tailrec
case class PalindromeProducts(start: Int, end: Int) {
  type Result = (Int, Set[(Int, Int)])
  def isPali(number: Int): Boolean = {
    @tailrec def reverse(n: Int, acc: Int = 0): Int = 
      if(n <= 0) acc
      else reverse(n / 10, acc * 10 + n % 10)
    reverse(number) == number
  }

  lazy val palindromes: List[Result] = {
    (start to end).foldLeft(List[Result]()) {(acc, n) =>
      val xs = (1 to n).foldLeft(Set[(Int, Int)]()){ (acc, x) => 
        if(isPali(n * x)) acc.+((x, n))
        else acc
      } 
      (n, xs) :: acc
    }
  }

  def smallest: Option[Result] = Some(palindromes.last)
  def largest: Option[Result] = Some(palindromes.head)
}
