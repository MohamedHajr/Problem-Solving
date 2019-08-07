object Raindrops {
  val translation: Map[Int, String] = Map(3 -> "Pling", 5 -> "Plang", 7 -> "Plong")
  def convert(n: Int): String = {  
    val result = translation.filterKeys(n % _ == 0).values.mkString
    if(result == "") n.toString else result
  }
}

