object Hamming {
  def difference(in: (Char, Char)): Int = if(in._1 != in._2) 1 else 0
  def distance(dna1: String, dna2: String): Option[Int] = 
    if(dna1.size != dna2.size) None
    else 
      Some(dna1.zip(dna2).foldRight(0)((chars, acc) => acc + difference(chars)))
}
