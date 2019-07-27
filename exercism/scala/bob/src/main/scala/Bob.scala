object Bob {
  def response(statement: String): String = {
    val alphabit = ('a' to 'z') ++ ('A' to 'Z') 
    def isQuestion(str: String) = str.endsWith("?")
    def isYelling(str: String) = str.exists(alphabit.toSet) && str.forall(c => c.isUpper || !c.isLetter)

    statement.trim match {
      case str if str.isEmpty => "Fine. Be that way!"
      case str if isQuestion(str) && isYelling(str) => "Calm down, I know what I'm doing!"
      case str if isQuestion(str) => "Sure."
      case str if isYelling(str) => "Whoa, chill out!"
      case _ => "Whatever."
    }
  }
}
