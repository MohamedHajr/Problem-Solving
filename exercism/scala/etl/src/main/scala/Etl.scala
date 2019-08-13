object Etl {
  def transform(oldData: Map[Int, Seq[String]]): Map[String, Int] = oldData
    .map { case (key, seq) => seq.map(_.toLowerCase -> key).toMap }
    .fold(Map.empty)(_ ++ _)
}
