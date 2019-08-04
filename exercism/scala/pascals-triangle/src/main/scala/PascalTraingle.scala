object PascalsTriangle {
  def getNextRow(prev: List[Int]) = (0 +: prev) zip (prev :+ 0) map { case (l, r) => l + r }
  def rows(n: Int): List[List[Int]] = {
    def rows: Stream[List[Int]] =  Stream.iterate(List(1))(getNextRow)
    rows take n toList
  }
}
