object Etl {
  def transform(oldData: Map[Int, Seq[String]]): Map[String, Int] = oldData
    .flatMap { case (key, seq) => seq.map(_.toLowerCase -> key).toMap }
}
