import java.time.{DayOfWeek, LocalDate}

import Schedule.Schedule
import java.time.temporal.TemporalAdjusters.{firstInMonth, lastInMonth, nextOrSame};


case class Meetup(month: Int, year: Int) {

  lazy val startOfMonth = LocalDate.of(year, month, 1)

  def day(dayOfWeek: Int, schedule: Schedule): LocalDate = {
    lazy val first = startOfMonth.`with`(firstInMonth(DayOfWeek.of(dayOfWeek)))
    schedule match {
      case Schedule.Teenth => startOfMonth.withDayOfMonth(13).`with`(nextOrSame(DayOfWeek.of(dayOfWeek)))
      case Schedule.First => first
      case Schedule.Second => first.plusDays(7)
      case Schedule.Third => first.plusDays(14)
      case Schedule.Fourth => first.plusDays(21)
      case Schedule.Last => startOfMonth.`with`(lastInMonth(DayOfWeek.of(dayOfWeek)))
    }
  }
  
}

object Schedule extends Enumeration {
  type Schedule = Value
  val Teenth, First, Second, Third, Fourth, Last = Value
}

object Meetup {
  val Mon = DayOfWeek.MONDAY.getValue
  val Tue = DayOfWeek.TUESDAY.getValue
  val Wed = DayOfWeek.WEDNESDAY.getValue
  val Thu = DayOfWeek.THURSDAY.getValue
  val Fri = DayOfWeek.FRIDAY.getValue
  val Sat = DayOfWeek.SATURDAY.getValue
  val Sun = DayOfWeek.SUNDAY.getValue
}
