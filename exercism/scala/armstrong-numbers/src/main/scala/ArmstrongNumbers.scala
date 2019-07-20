import math.pow

object ArmstrongNumbers {
    def isArmstrongNumber(num: Int): Boolean = {
        val digits =  num.toString
        val digitalize: Char => Int = _.asDigit
        val power: Int => Double = pow(_, digits.size)
        digits.map(digitalize andThen power).sum == num
    }
}
