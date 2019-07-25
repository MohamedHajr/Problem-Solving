object Bob {
  def response(statement: String): String = {
    if(statement.trim == "") return "Fine. Be that way!"

    val filters = (('a' to 'z' toList) ::: ('A' to 'Z' toList) ::: ('?' :: '!' :: Nil)) toSet
    val filterdStatement = statement.filter(filters)

    val isQuestion =  filterdStatement.endsWith("?")
    val isYelling = filterdStatement.size > 2 && filterdStatement.forall(c => c.isUpper || c == '!' || c == '?') 
    println(s"statement -> $filterdStatement, question -> $isQuestion, yelling -> $isYelling")

    (isQuestion, isYelling) match {
      case (true, true) => "Calm down, I know what I'm doing!"
      case (true, false) => "Sure."
      case (false, true) => "Whoa, chill out!"
      case (_, _) => "Whatever."
    }
  }
}
