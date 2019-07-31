object SpaceAge {
  val earthOrbitalPeriod: Double = 31557600
  val plantsYears = Map[String, Double](
    "mercury" ->  0.2408467,
    "venus" ->  0.61519726,
    "mars" -> 1.8808158,
    "jupiter" -> 11.862615,
    "saturn" -> 29.447498,
    "uranus" -> 84.016846,
    "neptune" -> 164.79132,
    "earth" -> 1
  ) 

  def calcYearsFor(seconds: Double, plant: String): Double = seconds / earthOrbitalPeriod / plantsYears(plant)

  def onEarth(seconds: Double): Double = calcYearsFor(seconds, "earth")
  def onMercury(seconds: Double): Double = calcYearsFor(seconds, "mercury")
  def onVenus(seconds: Double): Double =  calcYearsFor(seconds, "venus")
  def onMars(seconds: Double): Double =   calcYearsFor(seconds, "mars")
  def onJupiter(seconds: Double): Double = calcYearsFor(seconds, "jupiter")
  def onSaturn(seconds: Double): Double =  calcYearsFor(seconds, "saturn")
  def onUranus(seconds: Double): Double =  calcYearsFor(seconds, "uranus")
  def onNeptune(seconds: Double): Double = calcYearsFor(seconds, "neptune") 

}
