class Solution {
    fun solution(n: Int, left: Long, right: Long): MutableList<Int> {
        val result = mutableListOf<Int>()
        
        for (index in left..right) {
            // index를 기반으로 행과 열 인덱스를 계산
            val row = (index / n).toInt()
            val col = (index % n).toInt()
            
            // 행렬 값 계산: max(row, col) + 1
            result.add(maxOf(row, col) + 1)
        }
        
        return result
    }
}
