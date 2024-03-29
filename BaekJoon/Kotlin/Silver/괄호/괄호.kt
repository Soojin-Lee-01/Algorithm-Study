import java.io.BufferedReader
import java.util.Stack
import kotlin.system.exitProcess

fun main() = with(System.`in`.bufferedReader()) {
    val num = readLine().toInt()


    repeat(num) {
        var check = 0
        val data = readLine()!!.toList()
        var stack = Stack<String>()
        for(i in 0 until data.size) {
            if (data[i] == '(') {
                stack.push(data[i].toString())
            }
            else {
                if (stack.size > 0) {
                    stack.pop()
                }
                else {
                    println("NO")
                    check = -1
                    break
                }
            }
        }
        if (check != -1) {
            if (stack.size == 0) {
                println("YES")
            } else {
                println("NO")
            }
        }
    }
}