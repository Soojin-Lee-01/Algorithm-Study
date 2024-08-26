class Solution {
    fun solution(x: Int, n: Int): MutableList<Long> {
        var answer = mutableListOf<Long>()
        var first : Long = x.toLong()
        var plus : Long = x.toLong()
        repeat(n) {
            answer.add(first)
            first += plus
        }    
        return answer
    }
}
