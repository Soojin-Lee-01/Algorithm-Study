class Solution {
    fun solution(s: String): IntArray {
        var temp = s.toCharArray().map { it.toString().toInt() } // 문자열은 문자배열로 바꾸고 각 문자를 문자열로 변환 후 정수로 변환
        var count = 0
        var number = 0
        
        while (temp.size > 1) {
            var data = mutableListOf<Int>()
            for (i in 0 until temp.size) {
                if (temp[i] == 0) {
                    count++
                } else {
                    data.add(temp[i])
                }
            }
            number++
            temp = Integer.toBinaryString(data.size).toCharArray().map { it.toString().toInt() }
        }
        
        return intArrayOf(number, count)
    }
}
