import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue

fun main() {
    val sb = StringBuilder()
    var caseNum = 1
    val br = BufferedReader(InputStreamReader(System.`in`))

    while (true) {
        val (n, m) = br.readLine().split(" ").map { it.toInt() }
        if (n == 0 && m == 0) {
            break
        }

        val adj = Array(n + 1) { mutableListOf<Int>() }

        repeat(m) {
            val (u, v) = br.readLine().split(" ").map { it.toInt() }
            adj[u].add(v)
            adj[v].add(u)
        }

        val visited = BooleanArray(n + 1)
        var treeCount = 0

        for (i in 1..n) {
            if (!visited[i]) {
                if (isTreeComponent(i, adj, visited)) {
                    treeCount++
                }
            }
        }

        sb.append("Case ${caseNum++}: ")
        when (treeCount) {
            0 -> sb.append("No trees.\n")
            1 -> sb.append("There is one tree.\n")
            else -> sb.append("A forest of $treeCount trees.\n")
        }
    }
    println(sb)

}

fun isTreeComponent(startNode: Int, adj: Array<MutableList<Int>>, visited: BooleanArray): Boolean {
    var nodeCount = 0
    var edgeDegreeSum = 0

    val queue: Queue<Int> = LinkedList()
    queue.add(startNode)
    visited[startNode] = true

    while (queue.isNotEmpty()) {
        val current = queue.poll()
        nodeCount++
        edgeDegreeSum += adj[current].size

        for (neighbor in adj[current]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true
                queue.add(neighbor)
            }
        }
    }

    val edgeCount = edgeDegreeSum / 2
    return edgeCount == nodeCount - 1
}
