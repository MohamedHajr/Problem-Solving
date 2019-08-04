case class WordCount(word: String) {
  def countWords: Map[String, Int] = word
    .toLowerCase
    .split("\\W'|'\\W|[^\\w']")
    .filterNot(_.isEmpty) 
    .groupBy(identity)
    .mapValues(_.size)
}
