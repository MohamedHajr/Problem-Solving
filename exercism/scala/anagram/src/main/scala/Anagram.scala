object Anagram {
  
  def isAnagram(word: String)(matching: String): Boolean = 
      word.zip(matching).foldLeft(0)((acc, chars) => (acc ^ chars._1.asDigit) ^ chars._2.asDigit) == 0
  
  def findAnagrams(word: String, matches: List[String]): List[String] = 
    matches
      .filter(word.size == _.size)
      .filter(word.toLowerCase != _.toLowerCase)
      .filter(isAnagram(word))
}
