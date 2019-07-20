case class Triangle(x: Double, y: Double, z: Double) {
    def noZeros: Boolean = Set(x,y,z).min > 0
    def isEqual: Boolean = (x + y >= z) && (y + z >= x) && (z + x >= y)

    def noEqualSides: Boolean = Set(x, y, z).size == 3
    def twoEqualSides: Boolean = Set(x, y, z).size == 2  
    def allSidesEqual: Boolean = Set(x, y, z).size == 1

    def equilateral: Boolean = noZeros && isEqual && allSidesEqual
    def isosceles: Boolean = noZeros && isEqual && (allSidesEqual || twoEqualSides)
    def scalene: Boolean = noZeros && isEqual && noEqualSides
}
