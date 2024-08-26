
class Solution {
    fun solution(s: String): String {
        var answer = ""
        val strList = s.split(" ").map { it.toInt() }

        val max = strList.maxOrNull() ?: 0
        val min = strList.minOrNull() ?: 0

        answer = "$min $max"

        return answer
    }
}

