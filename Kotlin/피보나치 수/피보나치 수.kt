class Solution {
    fun solution(n: Int): Int {
        if (n == 0) return 0
        if (n == 1) return 1

        val map = IntArray(n+1)
        map[0] = 0
        map[1] = 1

        for (i in 2 until n+1) {
            map[i] = (map[i - 1] + map[i - 2]) % 1234567
        }

        return map[n]
    }
}


