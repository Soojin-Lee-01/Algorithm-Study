import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.system.exitProcess

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))

    val (r, c) = br.readLine().split(' ').map { it.toInt() }

    var graph = mutableListOf<MutableList<Char>>()

    for (i in 0 until r) {
        val data = br.readLine().map { it.toChar() }.toMutableList()
        graph.add(data)
    }

    fun bfs(r :Int, c : Int) : Boolean {
        val queue : Deque<Pair<Int, Int>> = LinkedList()
        queue.add(Pair(r, c))
        val direction = listOf(Pair(-1, 0), Pair(0, -1), Pair(1, 0), Pair(0, 1))

        while (queue.isNotEmpty()) {
            var (cur_r, cur_c) = queue.poll()
            for ((dx, dy) in direction) {
                val next_r = cur_r + dx
                val next_c = cur_c + dy

                if (next_r >= 0 && next_r < graph.size && next_c >= 0 && next_c < graph[0].size) {
                    if (graph[next_r][next_c] == 'S') {
                        return false
                    }
                }

            }
        }
        return true
    }

    var result = -1
    for ( i in 0 until r) {
        for ( j in 0 until c) {
            if (graph[i][j] == 'W') {
                if (bfs(i, j) == false) {
                    result = 0
                    break
                } else {
                    result = 1
                    break
                }
            }
        }
    }
    if (result == 0) {
        println(0)
    } else {
        println(1)
        for (i in 0 until r) {
            for (j in 0 until c) {
                if (graph[i][j] == '.') {
                    graph[i][j] = 'D'
                }
                print(graph[i][j])
            }
            println()
        }

    }



}
