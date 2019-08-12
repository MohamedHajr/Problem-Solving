object RotationalCipher {
  def rotateSmall(char: Char, shifts: Int): Char = {
    val shiftedChar = (char + shifts) % 123 
    if(shiftedChar < 97) (97 + shiftedChar).toChar
    else shiftedChar.toChar
  }
  
  def rotateCaptial(char: Char, shifts: Int): Char = {
    val shiftedChar = (char + shifts) % 91
    if(shiftedChar < 65) (65 + shiftedChar).toChar
    else shiftedChar.toChar
  }

  def rotate(sentence: String, shifts: Int): String= sentence map {
    case char if char.isUpper => rotateCaptial(char, shifts)
    case char if char.isLower=> rotateSmall(char, shifts)
    case c => c
  } 

}
