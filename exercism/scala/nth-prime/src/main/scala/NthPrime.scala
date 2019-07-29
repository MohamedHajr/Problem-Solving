object NthPrime {
  def getNextPrime(prime: Long): Stream[Long] = 
      Stream.iterate(prime + 2)(_ + 2).filter(isPrime)
    
  val primes: Stream[Long] = Stream.cons[Long](2, getNextPrime(1))

  def isPrime(number: Long): Boolean = 
      primes.takeWhile(_ <= math.sqrt(number)).forall(number % _ != 0)
   
  def prime(n: Int): Option[Long] = n match {
    case 0 => None
    case _ => Some(primes.take(n).last)
  }
}
