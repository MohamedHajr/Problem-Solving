import java.util.concurrent.Executors
import concurrent.duration.DurationInt
import scala.concurrent.{Await, ExecutionContext, Future}

object Frequency {
  implicit class improvedMap[A](val zis: Map[A, Int])(implicit num: Numeric[Int]) {
    def |+|(that: Map[A, Int]): Map[A, Int] =  {
      //Using groupMap in scala 2.13
      val merged = zis.toSeq ++ that.toSeq
      val grouped = merged.groupBy(_._1)
      grouped.mapValues(_.map(_._2).sum)
    }
  }

  def calcFrequency(text: String): Map[Char, Int] = text.groupBy(identity).mapValues(_.size)

  def filter(text: String): String =  text.toLowerCase.filter(_.isLetter)

  def frequency(numWorkers: Int, texts: Seq[String]): Map[Char, Int] = {
    implicit  val threadPool = ExecutionContext.fromExecutor(Executors.newWorkStealingPool(numWorkers))
    val frequencies = texts.map { text => Future { calcFrequency(filter(text)) } }
    val futureFrequencies = Future.fold(frequencies)(Map[Char, Int]())(_ |+| _)
    Await.result(futureFrequencies, 10 seconds)
  }
}

