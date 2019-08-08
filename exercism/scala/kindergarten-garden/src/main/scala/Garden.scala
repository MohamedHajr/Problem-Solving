object Plant {

  sealed trait Plant

  case object Clover extends Plant
  case object Grass extends Plant
  case object Violets extends Plant
  case object Radishes extends Plant

  def letterToPlant(char: Char): Plant = char match {
    case 'V' => Plant.Violets
    case 'C' => Plant.Clover
    case 'G' => Plant.Grass
    case 'R' => Plant.Radishes
  }
}

case class Garden(rows: String, kids: Seq[String]) {
  import Plant.{Plant, letterToPlant}

  def extractAndTransform(row: String, drop: Int): List[Plant] = row.drop(drop).take(2).map(letterToPlant).toList

  def plants(child: String): List[Plant] = {
    val Array(row1, row2, _*) = rows.split("\n")
    val startPosition = kids.indexOf(child) * 2
    extractAndTransform(row1, startPosition) ::: extractAndTransform(row2, startPosition)
  }
}

object Garden {
  private val kids = Array(
    "Alice", "Bob", "Charlie", "David",
    "Eve", "Fred", "Ginny", "Harriet",
    "Ileana", "Joseph", "Kincaid", "Larry"
  )
  def defaultGarden(rows: String): Garden = new Garden(rows, kids)
}
