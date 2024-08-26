import java.io.BufferedReader
import java.io.InputStreamReader


fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val test = readLine().toInt()
    repeat(test) {

        var num = readLine().toInt()
        var word = readLine()!!.split(" ").map {it.toInt()}
        val result = ArrayList(word)
        println("${result.min()} ${result.max()}")
    }

}