import math.pow

object ArmstrongNumbers {
    def digits(num: Int): List[Int] = num.toString.map(_.asDigit).toList
    def isArmstrongNumber(num: Int): Boolean = {
        val digitsList = digits(num)
        digitsList.fold(0)((acc, x) => acc + pow(x,digitsList.size).toInt)  == num
    }
}
