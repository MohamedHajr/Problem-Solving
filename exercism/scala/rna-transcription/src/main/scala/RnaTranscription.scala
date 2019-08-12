object RnaTranscription {
  private val translation = Map(
    'G' -> 'C',
    'C' -> 'G',
    'T' -> 'A',
    'A' -> 'U'
    )

  def toRna(rna: String): Option[String] = Some(rna map translation)
}
