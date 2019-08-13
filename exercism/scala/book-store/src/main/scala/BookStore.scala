object BookStore {
  private val bookPrice = 800
  private val discounts = Map(
    2 -> bookPrice * .05,
    3 -> bookPrice * .1,
    4 -> bookPrice * .2,
    5 -> bookPrice * .25
    )

  def calcBooksPrice(n: Int): Int = n * (bookPrice - discounts(n).toInt)

  def noDiscounts(books: List[Int]): Int = books.size * bookPrice 

  def calcTotal(start: Int, books: List[Int], total: Int = 0): Int = start match {
    case 1 => noDiscounts(books) + total
    case _ if books.toSet.size >= start => calcTotal(start, books diff books.toSet.take(start).toList, total + calcBooksPrice(start))
    case _ => calcTotal(start - 1, books, total)
  }
    
  def total(books: List[Int]): Int = Set(calcTotal(5, books), calcTotal(4, books), calcTotal(3, books), calcTotal(2, books)).min
}
