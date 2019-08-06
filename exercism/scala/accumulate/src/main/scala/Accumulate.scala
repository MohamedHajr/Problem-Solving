import scala.annotation.tailrec
class Accumulate {
  def accumulate[A, B](f: (A) => B, list : List[A]): List[B] = {
    @tailrec def transfer(inialList: List[A], resultList: List[B]): List[B] = inialList.headOption match {
      case None => resultList
      case Some(a) => transfer(inialList.tail, f(a) :: resultList) 
    } 
    transfer(list, List.empty).reverse
  }
}
