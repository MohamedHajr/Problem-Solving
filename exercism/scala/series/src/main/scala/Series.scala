import scala.annotation.tailrec
object Series {
  def slices(slices: Int, series: String): List[List[Int]] = {
    @tailrec def go(acc: List[List[Int]], series: String): List[List[Int]] = series.size match {
      case size if size < slices => acc
      case s => go(series.take(slices).toList.map(_.asDigit) :: acc, series.drop(1))
    }
    go(List.empty, series).reverse
  }
}
