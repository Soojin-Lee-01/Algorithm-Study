import java.io.BufferedReader
import java.io.InputStreamReader


fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    var student = ArrayList<Int>()

    repeat(28) {
        var num = readLine().toInt()
        student.add(num)
    }
    var result = ArrayList<Int>()
    for(i in 0 until 30) {
        if(i+1 !in student) {
            result.add(i+1)
        }
    }
    println(result.min())
    println(result.max())
}