object Darts {
  def score(x: Double, y: Double): Int = math.hypot(x,y) match {
    case x if x > 10 => 0
    case x if x > 5 => 1
    case x if x > 1 => 5
    case _ => 10
  }
}
