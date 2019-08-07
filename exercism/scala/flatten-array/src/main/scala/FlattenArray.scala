object FlattenArray {
  def flatten(current: List[Any]): List[Int] = current flatMap {
    case y :: ys => flatten(y :: ys)
    case x: Int => List(x)
    case _ => List()
  }
}
