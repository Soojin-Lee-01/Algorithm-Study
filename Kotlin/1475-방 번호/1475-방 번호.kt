import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var num = br.readLine()

    var data = mutableListOf<Int>()
    for(i in 0 until 10) {
        data.add(0)
    }

    for (i in 0 until num.length) {
        if (num[i].toString().toInt() == 6 || num[i].toString().toInt() == 9) {
            if (data[6] <= data[9]) {
                data[6] += 1
            } else {
                data[9] += 1
            }
        } else {
            data[num[i].toString().toInt()] += 1
        }
    }

    println(data.maxOrNull() ?: 1)


}
