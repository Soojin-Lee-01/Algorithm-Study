import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.min
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (n, d, k, c) = br.readLine().split(" ").map { it.toInt() }

    val data = mutableListOf<Int>()

    repeat(n) {
        var num = br.readLine().toInt()
        data.add(num)
    }
    data += data
    var ind = 0
    for (i in 0 until data.size/2) {
        var temp = data.subList(i, i+k)
        temp = temp.toMutableSet().toMutableList()
        if (c in temp) {
            if (ind < temp.size-1) {
                ind = temp.size-1
            }
        } else {
            if (ind < temp.size) {
                ind = temp.size
            }
        }

    }
    println(ind+1)

}
