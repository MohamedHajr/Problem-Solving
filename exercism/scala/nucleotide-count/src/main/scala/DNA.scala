case class DNA(dna: String) {
  def nucleotideCounts: Either[Unit, Map[Char, Int]] = dna match {
    case xs if xs == "" => Right(DNA.empty)
    case xs if xs.toSet.size > 4 => Left()
    case _ => Right(DNA.empty ++ dna.groupBy(identity).mapValues(_.size))
  }  
}

object DNA {
  def empty: Map[Char, Int] = Map('A' -> 0, 'C' -> 0, 'G' -> 0, 'T' -> 0)
}
