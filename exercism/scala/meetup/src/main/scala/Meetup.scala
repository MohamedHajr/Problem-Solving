import java.time.{DayOfWeek, LocalDate}

import Schedule.Schedule
import java.time.temporal.TemporalAdjusters.{firstInMonth, lastInMonth, nextOrSame};


case class Meetup(month: Int, year: Int) {

  lazy val startOfMonth = LocalDate.of(year, month, 1)

  def day(dayOfWeek: DayOfWeek, schedule: Schedule): LocalDate = {
    lazy val first = startOfMonth.`with`(firstInMonth(dayOfWeek))
    schedule match {
      case Schedule.Teenth => startOfMonth.withDayOfMonth(13).`with`(nextOrSame(dayOfWeek))
      case Schedule.First => first
      case Schedule.Second => first.plusDays(7)
      case Schedule.Third => first.plusDays(14)
      case Schedule.Fourth => first.plusDays(21)
      case Schedule.Last => startOfMonth.`with`(lastInMonth(dayOfWeek))
    }
  }
  
}

object Schedule extends Enumeration {
  type Schedule = Value
  val Teenth, First, Second, Third, Fourth, Last = Value
}

object Meetup {
  val Mon = DayOfWeek.MONDAY
  val Tue = DayOfWeek.TUESDAY
  val Wed = DayOfWeek.WEDNESDAY
  val Thu = DayOfWeek.THURSDAY
  val Fri = DayOfWeek.FRIDAY
  val Sat = DayOfWeek.SATURDAY
  val Sun = DayOfWeek.SUNDAY
}
