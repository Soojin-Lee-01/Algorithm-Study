import java.util.Stack

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
fun main() = with(System.`in`.bufferedReader()) {
    var stack = Stack<Int>()

    val num = readLine().toInt()

    repeat(num) {
        var data = readLine().split(" ").map { it.toString() }
        val a = if (data.size > 1) data[1].toInt() else 0
        val b = data[0]

        if (b == "push") {
            stack.push(a)
        }
        else if(b == "pop") {
            if (stack.isEmpty()) {
                println(-1)
            } else {
                println(stack.pop())
            }
        }
        else if(b == "size") {
            println(stack.size)
        }
        else if(b == "empty") {
            if (stack.isEmpty()) {
                println(1)
            }
            else {
                println(0)
            }
        }
        else {
            if (stack.isEmpty()) {
                println(-1)
            } else {
                println(stack.peek())
            }
        }
    }

}