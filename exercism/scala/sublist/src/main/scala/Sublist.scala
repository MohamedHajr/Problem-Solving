
object Sublist {
  sealed trait Sublist

  case object Sublist extends Sublist
  case object Equal extends Sublist
  case object Unequal extends Sublist
  case object Superlist extends Sublist

  def isSubSet(xs: List[Int], ys: List[Int]): Boolean = 
    xs.isEmpty || ys.sliding(xs.size).exists(_ == xs)

  def sublist(xs: List[Int], ys: List[Int]): Sublist = xs match {
    case xs if xs == ys => Equal
    case xs if isSubSet(ys, xs) => Superlist
    case xs if isSubSet(xs, ys) => Sublist
    case _ => Unequal
  }
  
}
