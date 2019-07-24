object MatchingBrackets {
  def isPaired(str: String): Boolean = {
    def go(brackets: List[Char], stack: List[Char]): Boolean = 
      (brackets, stack) match {
        case (Nil, Nil) => true
        case (('{' | '[' | '(')::xs, _) => go(xs, brackets.head :: stack)
        case ('}'::xs, '{'::ys) => go(xs, ys) 
        case (']'::xs, '['::ys) => go(xs, ys) 
        case (')'::xs, '('::ys) => go(xs, ys) 
        case _ => false
      }
    go(str.filter("(){}[]".toSet).toList, List())
  }
}
