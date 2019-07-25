object PascalsTriangle {
  def constructRow(list: List[Int])  = 1 :: list :: List(1)  toStream
  def getNextRow(curr: List[Int]) = constructRow(curr.zip(curr.tail).map(row => row._1 + row._2))
  def rows(n: Int): List[List[Int]] = {
    def rows(previous: List[Int] = List(1,1)): Stream[List[Int]] =  previous #:: getNextRow(previous) 
    rows() take n toList
  }
}
