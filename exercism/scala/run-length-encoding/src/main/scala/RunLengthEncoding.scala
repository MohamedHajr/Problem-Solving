object RunLengthEncoding {
  def encode(text: String, acc: String = ""): String =  text match {
    case "" => acc
    case _ =>  {
     val (matches, rest) = text.span(_ == text.head)
     val encodedChunk = if (matches.length == 1) matches else matches.length.toString + matches.head
     encode(rest, acc ++ encodedChunk)
    }
  }
   
  
  def decode(cypher: String, decoded: String = ""): String = cypher match {
    case "" => decoded
    case _ => {
      val (number, rest) = cypher.span(_.isDigit)
      val decodedChunk = if(number == "") rest.head.toString else rest.head.toString * number.toInt 
      decode(rest.tail, decoded ++ decodedChunk)
    }
  }
     
}
