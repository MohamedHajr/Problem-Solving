object FlattenArray {
  def flatten(current: List[Any], acc: List[Any] = List.empty): List[Any] = current match {
    case Nil => acc
    case null :: xs => flatten(xs, acc)
    case (y :: ys) :: xs => flatten(y :: ys) ::: flatten(xs, acc)
    case x :: xs => flatten(xs, x :: acc)
  }

}
