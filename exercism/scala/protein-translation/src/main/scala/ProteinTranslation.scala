object ProteinTranslation {
  def proteins(dna: String): Seq[String] = {
    val CODONS= Map(
      "UAA" -> "STOP",
      "UAG" -> "STOP",
      "UGA" -> "STOP",
      "UGG" -> "Tryptophan",
      "UGU" -> "Cysteine",
      "UGC" -> "Cysteine",
      "UAU" -> "Tyrosine",
      "UAC" -> "Tyrosine",
      "UCU" -> "Serine",
      "UCC" -> "Serine",
      "UCA" -> "Serine",
      "UCG" -> "Serine",
      "UUA" -> "Leucine",
      "UUG" -> "Leucine",
      "UUU" -> "Phenylalanine",
      "UUC" -> "Phenylalanine",
      "AUG" -> "Methionine"
    )
    dna.grouped(3).takeWhile(CODONS(_) != "STOP").map(CODONS(_)).toSeq
  }
}
