object RunLengthEncoding {
  def encode(text: String, acc: String = ""): String =  text match {
    case "" => acc
    case _ =>  {
     val matches = text.takeWhile(text.head == _)
     if(matches.size > 1)
      encode(text.drop(matches.size), acc ++ s"${matches.size}${matches.head}")
     else
      encode(text.drop(1), acc ++ matches.head.toString)   
    }
  }
   
  
  def decode(cypher: String): String = {
    
  }
}
