import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import kotlin.math.abs
import kotlin.math.min


fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()

    val graph : MutableList<List<Int>> = mutableListOf()

    repeat(n) {
        val data = br.readLine().split(" ").map{it.toInt()}.toList()
        graph.add(data)
    }

    val result : Deque<List<Int>> = LinkedList()

    val person = mutableListOf<Int>()
    for (i in 1 until n+1) {
        person.add(i)
    }

    fun combination(num:Int, start:Int = 0, combo : MutableList<Int> = mutableListOf()) {
        if (combo.size == num) {
            result.add(combo.toList())
            return
        }
        for (i in start until person.size) {
            combo.add(person[i])
            combination(num, i+1, combo)
            combo.removeLast()
        }
    }

    combination(n/2)

    var final = 10e9

    while(result.size > 0) {
        var temp = result.removeFirst()
        var data1 = temp
        var data2 = mutableListOf<Int>()

        for (k in 1 until n+1) {
            if (k !in data1) {
                data2.add(k)
            }
        }
        var data1_sum = 0
        for(a in 0 until data1.size) {
            for (b in a until data1.size) {
                data1_sum += graph[data1[a]-1][data1[b]-1]
                data1_sum += graph[data1[b]-1][data1[a]-1]

            }
        }
        var data2_sum = 0
        for (a in 0 until data2.size) {
            for (b in a until data2.size) {
                data2_sum += graph[data2[a]-1][data2[b]-1]
                data2_sum += graph[data2[b]-1][data2[a]-1]
            }
        }
        if (abs(data1_sum-data2_sum) < final) {
            final = abs(data1_sum-data2_sum).toDouble()
        }


    }
    println(final.toInt())

}
