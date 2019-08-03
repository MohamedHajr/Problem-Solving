class School {
  type DB = Map[Int, Seq[String]]

  var db: DB =  Map()

  def add(name: String, g: Int) =  {
    db = db + (g -> (grade(g).:+(name)))
  }

  def grade(g: Int): Seq[String] = db.getOrElse(g, Seq())

  def sorted: DB =  Map(db.toSeq.sortBy(_._1): _*).map{ case (key, value) => (key, value.sorted) } 

}
