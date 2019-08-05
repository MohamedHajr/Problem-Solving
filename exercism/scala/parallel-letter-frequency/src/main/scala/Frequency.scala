object Frequency {
  def calcFrequency(text: String): Map[Char, Int] = text.groupBy(identity).mapValues(_.size)
  def frequency(numWorkers: Int, texts: Seq[String]): Map[Char, Int] =  texts
    .map(_.toLowerCase.trim)
    .map(_.filter(_.isLetter))
    .map(calcFrequency)
    .fold(Map())(_ ++ _)
}
