class Solution {
    fun solution(strings: Array<String>, n: Int): List<String> {
       
       strings.sort()  
   
       return strings.sortedBy {it[n]}
    }
}
