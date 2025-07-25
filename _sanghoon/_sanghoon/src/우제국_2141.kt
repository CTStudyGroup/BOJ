import java.io.BufferedReader
import java.io.InputStreamReader

data class Village(
    val location: Long,
    val population: Long,
)
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()

    val villages = Array(N) { Village(0, 0)}
    var totalPopulation = 0L

    for (i in 0 until N) {
        val (x, a) = br.readLine().split(" ").map { it.toLong() }
        villages[i] = Village(x, a)
        totalPopulation += a;
    }

    villages.sortBy { it.location }

    var populationSum = 0L
    for (village in villages) {
        populationSum += village.population
        if (populationSum >= (totalPopulation + 1) / 2) {
            print(village.location)
            break
        }
    }
}