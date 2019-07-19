object CollatzConjecture {
    def steps(num: Int, step: Int = 0): Option[Int] = {
        num match {
            case 1 => Some(step)
            case x if(x > 0) => if(x % 2 == 0) steps(x / 2, step + 1) else steps(x * 3 + 1, step + 1)
            case _ => None
        }
    } 
}

