import java.util.LinkedList
import java.util.Queue

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m, v) = readLine().split(" ").map { it.toInt() }
    var list = ArrayList<ArrayList<Int>>()
    repeat(n + 1) {
        list.add(ArrayList<Int>())
    }

    repeat(m) {
        var (a, b) = readLine().split(" ").map { it.toInt() }
        list[a].add(b)
        list[b].add(a)

    }
    for (i in 0 until list.size) {
        list[i].sort()
    }
    val result = ArrayList<Int>()
    fun bfs(start: Int) {
        val visited = BooleanArray(n + 1)
        val queue: Queue<Int> = LinkedList()

        result.add(start)
        queue.offer(start)
        visited[start] = true
        while (queue.isNotEmpty()) {
            val cur_r = queue.poll()
            for (v in list[cur_r]) {
                if (!visited[v]) {
                    queue.offer(v)
                    visited[v] = true
                    result.add(v)
                }
            }
        }
    }

    var result2 = ArrayList<Int>()
    val visited2 = BooleanArray(n + 1)
    fun dfs(start: Int) {
        visited2[start] = true
        result2.add(start)
        for (next_v in list[start]) {
            if (!visited2[next_v]) {
                dfs(next_v)
            }
        }
    }

    dfs(v)
    println(result2.joinToString(" "))
    bfs(v)
    println(result.joinToString(" "))
}