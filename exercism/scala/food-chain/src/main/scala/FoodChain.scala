object FoodChain {
  val animals = Map[Int, String](
    1 -> "fly.",
    2 -> "spider.\nIt wriggled and jiggled and tickled inside her.",
    3 -> "bird.\nHow absurd to swallow a bird!",
    4 -> "cat.\nImagine that, to swallow a cat!",
    5 -> "dog.\nWhat a hog, to swallow a dog!",
    6 -> "goat.\nJust opened her throat and swallowed a goat!",
    7 -> "cow.\nI don't know how she swallowed a cow!",
    8 -> "horse.\nShe's dead, of course!"
  )     

  val verses: List[String] = 
    "I don't know why she swallowed the fly. Perhaps she'll die." ::
    "She swallowed the spider to catch the fly." ::
    "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her." ::
    "She swallowed the cat to catch the bird." ::
    "She swallowed the dog to catch the cat." ::
    "She swallowed the goat to catch the dog." ::
    "She swallowed the cow to catch the goat." :: 
    Nil
    
  
  def constructVerses(verse: Int): String = 
    if(verse != 8)
      "I know an old lady who swallowed a " ++ animals(verse) ++ "\n" ++ verses.take(verse).reverse.mkString("\n") ++ "\n\n" 
    else
      "I know an old lady who swallowed a " ++ animals(8) ++ "\n\n"

  def recite(start: Int, limit: Int): String = limit - start match {
    case 0 => constructVerses(start)
    case _ => (start to limit).map(constructVerses).mkString
  }  
   
}
