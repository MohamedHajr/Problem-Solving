object PhoneNumber {
  def clean(number: String): Option[String] = {
    val numberFormat = "(^[2-9]{3})([2-9]{3})([0-9]{4})".r
    number.filter(_.isDigit) match {
      case numberFormat(areaCode, exchageCode, rest) => Some(areaCode ++ exchageCode ++ rest)
      case _ => None
    }
  }
}

