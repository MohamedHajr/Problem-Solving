object Isogram {
    def isIsogram(word: String): Boolean = {
        val filtered = word.toLowerCase.filter(_.isLetter)
        filtered.toSet.size == filtered.size
    }
}
