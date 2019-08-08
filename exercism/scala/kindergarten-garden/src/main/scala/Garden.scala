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

case class Garden(rows: String) {
  import Plant.{Plant, letterToPlant}

  def extractAndTransform(row: String, drop: Int): List[Plant] = row.drop(drop).take(2).map(letterToPlant).toList
  def plants(child: String): List[Plant] = {
    val Array(row1, row2, _*) = rows.split("\n")
    child match {
      case "Alice" => extractAndTransform(row1, 0) ::: extractAndTransform(row2, 0)
      case "Bob" => extractAndTransform(row1, 2) ::: extractAndTransform(row2, 2)
      case "Charlie" => extractAndTransform(row1, 4) ::: extractAndTransform(row2, 4)
      case "Kincaid" => extractAndTransform(row1, 20) ::: extractAndTransform(row2, 20)
      case "Larry" => extractAndTransform(row1, 22) ::: extractAndTransform(row2, 22)
    }
  }
}

object Garden {
  private val kids = List(
    "Alice", "Bob", "Charlie", "David",
    "Eve", "Fred", "Ginny", "Harriet",
    "Ileana", "Joseph", "Kincaid", "Larry"
  )
  def defaultGarden(rows: String): Garden = new Garden(rows)
}
