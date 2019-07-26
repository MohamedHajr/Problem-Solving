import java.time.LocalDate
import java.time.LocalDateTime
import math.pow

object Gigasecond {
  def add(startDate: LocalDate): LocalDateTime = add(startDate.atStartOfDay)

  def add(startDateTime: LocalDateTime): LocalDateTime = startDateTime.plusSeconds(pow(10, 9).toLong)
}
