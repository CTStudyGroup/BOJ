import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

data class Beer(val preference: Int, val alcohol: Int) : Comparable<Beer> {
    // 도수 오름차순, 선호도 내림차순
    override fun compareTo(other: Beer): Int {
        return if (this.alcohol != other.alcohol) {
            this.alcohol - other.alcohol
        } else {
            other.preference - this.preference
        }
    }
}

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, m, k) = br.readLine().split(" ").map {it.toLong()}

    var beers = Array(k.toInt()) {
        val (v, c) = br.readLine().split(" ").map {it.toInt()}
        Beer(v, c)
    }

    beers.sort()

    val pq = PriorityQueue<Int>()
    var totalPreference = 0L
    var answer = -1

    for (beer in beers) {
        pq.add(beer.preference)
        totalPreference += beer.preference

        if (pq.size > n) {
            totalPreference -= pq.poll();
        }

        if (pq.size.toLong() == n && totalPreference >= m) {
            answer = beer.alcohol
            break
        }
    }

    println(answer)
}