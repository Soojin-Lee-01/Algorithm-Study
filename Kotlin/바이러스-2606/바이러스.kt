import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val num = readLine().toInt()
    val edge = readLine().toInt()
    val graph = ArrayList<ArrayList<Int>>()


    repeat(num+1) {
        graph.add(ArrayList())
    }
    repeat(edge) {
        var (a, b) = readLine().split(" ").map { it.toInt() }
        graph[a].add(b)
        graph[b].add(a)
    }
    var cnt = 0
    println(graph)
    fun bfs(start: Int) {
        val visited = BooleanArray(num+1)
        val queue : Queue<Int> = LinkedList()
        queue.offer(start)
        visited[start] = true

        while (queue.isNotEmpty()) {
            val cur_r = queue.poll()

            for (v in graph[cur_r]) {
                if(!visited[v]) {
                    visited[v] = true
                    cnt++
                    queue.offer(v)

                }
            }
        }

    }

    bfs(1)
    println(cnt)
}