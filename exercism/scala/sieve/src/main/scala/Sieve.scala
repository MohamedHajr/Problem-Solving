object Sieve {
   def primes(limit: Int): List[Int] = {
        if(limit <= 1) return List.empty
        def go(curr: List[Int], result: List[Int] = List.empty): List[Int] = 
            curr.headOption match {
                case None       => result
                case Some(head) => go(curr.tail.filter(_ % head != 0), result :+ head)
            } 
        go(2 to limit toList)
    }
}

