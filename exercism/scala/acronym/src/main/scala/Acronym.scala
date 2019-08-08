object Acronym {
  def abbreviate(phrase: String): String = phrase
    .split("[ -]")
    .filterNot(_.isEmpty)
    .map { case word => word.head.toUpper }
    .mkString
}
