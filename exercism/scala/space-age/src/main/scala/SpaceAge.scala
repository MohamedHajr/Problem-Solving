object SpaceAge {
  val earthOrbitalPeriod = 31557600
  val plantsYears = Map(
    "mercury" ->  0.2408467,
    "venus" ->  0.61519726,
    "mars" -> 1.8808158,
    "jupiter" -> 11.862615,
    "saturn" -> 29.447498,
    "uranus" -> 84.016846,
    "neptune" -> 164.79132,
    "earth" -> 1
  ) 

  def onEarth(seconds: Double): Double = seconds / earthOrbitalPeriod 
  def onMercury(seconds: Double): Double =  onEarth(seconds) / 0.2408467
  def onVenus(seconds: Double): Double =  onEarth(seconds) / 0.61519726
  def onMars(seconds: Double): Double =   onEarth(seconds) / 1.8808158
  def onJupiter(seconds: Double): Double = onEarth(seconds) / 11.862615 
  def onSaturn(seconds: Double): Double =  onEarth(seconds) / 29.447498 
  def onUranus(seconds: Double): Double =  onEarth(seconds) / 84.016846
  def onNeptune(seconds: Double): Double =  onEarth(seconds) / 164.79132
}
