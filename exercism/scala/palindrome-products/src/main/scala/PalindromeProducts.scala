import scala.annotation.tailrec
case class PalindromeProducts(start: Int, end: Int) {
  def isPali(number: Int): Boolean = {
    @tailrec def reverse(n: Int, acc: Int = 0): Int = 
      if(n <= 0) acc
      else reverse(n / 10, acc * 10 + n % 10)
    reverse(number) == number
  }

  lazy val palindromes = 
    for {
      i <- start to end
      j <- i to end
      if isPali(i * j)
    } yield (i * j, (i, j))
    
  type Result = (Int, Set[(Int, Int)])

  def selectPalindrome(selection: (Int, Int) => Int): Option[Result] = for (
      selected <- palindromes.map(_._1).reduceOption(selection(_, _));
      factors = palindromes.collect{ case (product, factors) if product == selected => factors }.sorted.toSet
    ) yield (selected, factors)
    
  def smallest: Option[Result] = selectPalindrome(math.min)
  def largest: Option[Result] = selectPalindrome(math.max)
}
