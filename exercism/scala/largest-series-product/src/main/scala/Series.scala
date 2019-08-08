object Series {
  def largestProduct(product: Int, digits: String): Option[Int] = product match {
    case 0 => Some(1)
    case _ if digits.isEmpty || digits.exists(!_.isDigit) || product < 0 || product > digits.size => None 
    case _ => Some(digits
        .sliding(product)
        .map(_.toList.map(_.asDigit).product).max)
  }
}

