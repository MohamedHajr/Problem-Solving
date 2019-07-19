
class Robot {
    var name = Robot.generateName()

    def reset(): Unit = name = Robot.generateName()
}

object Robot {
    import scala.util.Random

    private def genLetters(limit: Int) =  Random.alphanumeric.filter(_.isLetter).map(_.toUpper).take(limit).mkString 
    private val digit = ('0' to '9').toArray
    private val digitsSpec = List(digit, digit, digit)
    def digits : String = digitsSpec.map(collection(Random.nextInt(collection.length)(_))).mkString

    def generateName(charsLength: Int = 2): String = genLetters(charsLength) ++ digits
}