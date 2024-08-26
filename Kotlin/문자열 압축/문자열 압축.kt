class Solution {
    fun solution(s: String): Int {
        var answer = 0

        var temp = 1
        var result = Int.MAX_VALUE
        
        for (i in 1..s.length) {
            val data = mutableListOf<String>()
            for (j in 0 until s.length step i) {
                val end = minOf(j + temp, s.length)
                data.add(s.substring(j, end))
                
            }
            
            var te = ""
            var co = 0
            var tt = 0
            
            for (j in data.indices) {
                if (j == 0) {
                    te = data[j]
                    co += 1
                } else {
                    if (data[j] == te) {
                        co += 1
                    } else {
                        if (co == 1) {
                            tt += te.length
                        } else {
                            tt += co.toString().length + te.length
                        }
                        te = data[j]
                        co = 1
                    }
                }
            }
            
            if (co == 1) {
                tt += te.length
            } else {
                tt += co.toString().length + te.length
            }
            
            result = minOf(tt, result)
            temp += 1
        }

        return result
    }
}
