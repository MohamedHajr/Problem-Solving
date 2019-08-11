object PigLatin {
  private val vowelsAndCases =  Set('a', 'e', 'i', 'u', 'o', "xr", "yt")

  private val specialCases = Set("ch", "qu", "th", "thr", "sch")

  //pattern matching version
  def translateWord(word: String): String = word.toList match {
    case x :: y :: _  if (vowelsAndCases contains x) || (vowelsAndCases contains s"$x$y") => word ++ "ay"
    case x :: y :: z :: _ if specialCases contains(s"$x$y$z") => word.drop(3) ++ s"$x$y$z" ++ "ay"
    case x :: y :: _ if specialCases contains(s"$x$y") => word.drop(2) ++ s"$x$y" ++ "ay"
    case x :: 'q' :: 'u' :: _ => word.drop(3) ++ s"${x}qu" ++ "ay"
    case _ => word.drop(1) ++ word.take(1) ++ "ay"
  }

  //regex version
  def translateWord2(word: String): String = {
    val specialVowelsRegex = "^(xr|yt)(.*)$".r  
    val constant = """^(qu|y|[^aeiouy]qu|[^aeiouy]+)(.*)""".r

    word match {
      case specialVowelsRegex(first, last) => first ++ last ++ "ay"
      case constant(first, last) => last ++ first ++ "ay"
      case _ => word + "ay"
    }
  }

  def translate(word: String): String = word.split(" ").map(translateWord2).mkString(" ")
}
