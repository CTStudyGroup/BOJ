import java.io.BufferedReader
import java.io.InputStreamReader


lateinit var arr: Array<IntArray>
val sb = StringBuilder();

fun main(args:Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()

    arr = Array(N) { IntArray(N) }

    for (i in 0 until N) {
        val line = br.readLine()
        for (j in 0 until N) {
            arr[i][j] = line[j] - '0'
        }
    }
    recur(0, 0, N);
    println(sb)
}

fun recur(row: Int, col : Int, size: Int) {
    if (check(row, col, size)) {
        sb.append(arr[row][col])
        return
    }

    sb.append("(")

    val newSize = size / 2

    recur(row, col, newSize)
    recur(row, col + newSize, newSize)
    recur(row + newSize, col, newSize)
    recur(row + newSize, col + newSize, newSize)

    sb.append(")")
}

fun check(row: Int, col: Int, size: Int): Boolean {
    val firstValue = arr[row][col]
    for (r in row until row + size) {
        for (c in col until col + size) {
            if (arr[r][c] != firstValue) {
                return false;
            }
        }
    }
    return true
}
