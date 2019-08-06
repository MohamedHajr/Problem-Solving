object Frequency {
  implicit class improvedMap[A](val zis: Map[A, Int])(implicit num: Numeric[Int]) {
    def combine(that: Map[A, Int]): Map[A, Int] =  {
      val merged = zis.toSeq ++ that.toSeq
      val grouped = merged.groupBy(_._1)
      grouped.mapValues(_.map(_._2).sum)
    }
  }
  def calcFrequency(text: String): Map[Char, Int] = text.groupBy(identity).mapValues(_.size)

  def frequency(numWorkers: Int, texts: Seq[String]): Map[Char, Int] =  texts
    .map(_.filter(_.isLetter).toLowerCase.trim)
    .map(calcFrequency)
    .fold(Map())(_ combine _)
}

