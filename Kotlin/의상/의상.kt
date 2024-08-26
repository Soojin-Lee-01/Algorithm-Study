class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        val map = HashMap<String, Int>()
        for (i in 0 until clothes.size) {
            if(clothes[i][1] in map) {
                map[clothes[i][1]]  = map[clothes[i][1]]!! + 1
            } else {
                map.put(clothes[i][1], 1)
            }
        }

        var answer = 1
        for (i in map.values) {
            answer *= (i+1)
        }
        return answer-1
    }
}