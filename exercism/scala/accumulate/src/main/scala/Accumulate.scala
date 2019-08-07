import scala.annotation.tailrec
class Accumulate {
  def accumulate[A, B](f: (A) => B, list : List[A]): List[B] = {
    @tailrec def transfer(inialList: List[A], resultList: List[B]): List[B] = inialList match {
      case Nil => resultList
      case x::xs => transfer(xs, f(x) :: resultList) 
    } 
    transfer(list, List.empty).reverse
  }
}
