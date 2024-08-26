import java.io.BufferedReader
import java.io.InputStreamReader
/*
이 문제는 최소를 구해야하므로 "-"을 기준으로 split() 한 후,
split된 것을 각각 더한 후 마지막에 각각 숫자를 빼주면 최소가 된다!!
-> 아이디어를 잘 생각해야한다....!
 */
fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var data : MutableList<MutableList<String>> = mutableListOf()
    val word = br.readLine()
    var temp = mutableListOf<String>()
    // "-" 을 기준으로 split 해준다.
    temp = word.split("-").toMutableList()

    // "+" 을 기준으로 split 해준다.
    for (i in 0 until temp.size) {
        data.add(temp[i].split("+").toMutableList())
    }

    // "+" 을 기준으로 split 한것을 각각 더해준다.
    var final = mutableListOf<Int>()
    for (i in 0 until data.size) {
        var temp = 0
        for (j in 0 until data[i].size) {
            temp += data[i][j].toInt()
        }
        final.add(temp)
    }

    // 최종으로, 숫자들은 모두 빼준다.
    var result = 0
    for (i in 0 until final.size) {
        if (i == 0) {
            result = final[0]
        } else {
            result -= final[i]
        }
    }
    println(result)
}