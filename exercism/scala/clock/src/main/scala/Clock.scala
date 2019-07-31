case class Clock(hrs: Int, mins: Int) {
  def +(that: Clock): Clock = 
    Clock(this.hrs + that.hrs, this.mins + that.mins)
  def -(that: Clock): Clock = 
    Clock(this.hrs - that.hrs, this.mins - that.mins)
  override def equals(other: Any): Boolean = other.isInstanceOf[Clock] && hashCode == other.hashCode
  override def hashCode: Int = 31 * hrs * mins
}


object Clock { 
  import Math.{floorMod  => mod}
  import Math.{floorDiv => div}

  def apply(hrs: Int, mins: Int): Clock = new Clock(
    mod(div(mins, 60) + hrs, 24),
    mod(mins, 60)
  )
  def apply(mins: Int): Clock = apply(0, mins)
}

