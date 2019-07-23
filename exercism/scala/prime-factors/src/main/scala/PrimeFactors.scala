object PrimeFactors {
  def factors(number: Long, xs: List[Long] = List(), curr: Long = 2): List[Long] = 
    number match {
      case 1 => xs
      case x if x % curr == 0 => factors(number / curr, xs :+ curr, curr)
      case _ => factors(number, xs, curr+1)
    }
}

import scala.annotation.tailrec

case class PrimeFactors(){
    private val primes : Stream[Long] = Stream.cons[Long](2, getNextPrimes(1))

    private def isPrime(n : Long) =
        primes.takeWhile(_ <= math.sqrt(n)).forall(n % _ != 0)

    private def getNextPrimes(prime : Long): Stream[Long] =
        Stream.iterate(prime + 2)(_ + 2).filter(isPrime)

    @tailrec private def factors(num : Long, accu : List[Long] = Nil): List[Long] = num match {
        case 1 => accu.reverse
        case n =>
            val factor = primes.dropWhile( n % _ != 0).head
            factors(n / factor, factor :: accu)
    }

    def primeFactors(num : Long) = factors(num)
}
