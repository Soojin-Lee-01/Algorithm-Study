import java.io.BufferedReader

fun main() = with(System.`in`.bufferedReader()) {
    var (n, m) = readLine().split(" ").map { it.toInt() }
    var list = ArrayList<Int>()
    val data = readLine().split(" ").map { it.toInt() }
    for (i in 0 until data.size) {
        list.add(data[i])
    }
    repeat(m) {
        var (a, b, c) = readLine().split(" ").map { it.toInt() }
        if (a == 1) {
            list[b - 1] = c
        } else if (a == 2) {
            for (i in b - 1 until c) {
                if (list[i] == 1) {
                    list[i] = 0
                } else {
                    list[i] = 1
                }

            }
        } else if (a == 3) {
            for (i in b - 1 until c) {
                list[i] = 0
            }
        } else {
            for (i in b - 1 until c) {
                list[i] = 1
            }
        }
    }

    println(list.joinToString(" "))

}