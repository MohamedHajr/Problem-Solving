class School {
  type DB = Map[Int, Seq[String]]

  var db: DB =  Map.empty

  def add(name: String, g: Int) =  db += g -> (grade(g) :+ name)

  def grade(g: Int): Seq[String] = db.getOrElse(g, Seq())

  def sorted =  collection.SortedMap(db.toSeq:_*).mapValues(_.sorted) 

}
