import java.util.Deque
import java.util.LinkedList

class Solution {
    fun solution(x: Int, y: Int, n: Int): Int {
        // 처음부터 x와 y가 같은 경우 0을 반환
        if (x == y) {return 0}
        // bfs를 통해 탐색!
        fun bfs(start : Int) : Int {
            
            val queue : Deque<Pair<Int, Int>> = LinkedList()
            queue.add(Pair(start, 0))
            val visited = BooleanArray(10000000) {false}
            visited[start] = true
            
            while (queue.isNotEmpty()) {
                val (next, steps) = queue.poll()
                
                // n을 더하거나, 2를 곱하거나, 3을 곱하거나
                val nextValues = listOf(next + n, next * 2, next * 3)
                
                for (value in nextValues) {
                    // 만약에 y와 같아졌으면 반환
                    if (value == y) {return steps+1 }
                    if (!visited[value] && value <= 1000000) {
                        queue.add(Pair(value, steps+1))
                        visited[value] = true
                    }
                }
            }
            // x를 y로 만들 수 없다면 -1 반환       
            return -1
        }
        return bfs(x)
    }
}
