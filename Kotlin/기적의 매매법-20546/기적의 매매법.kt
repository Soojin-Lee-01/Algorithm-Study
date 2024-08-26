fun main() = with(System.`in`.bufferedReader()) {
    val cash = readLine().toInt()
    val list = readLine().split(" ").map { it.toInt() }

    // 준현
    var jun = 0
    var cash1 = cash
    for (i in 0 until 14) {
        if (list[i] <= cash1) {
            jun = (cash1 / list[i])
            cash1 -= (list[i] * jun)
        }
    }

    // 성민
    var sun = 0
    var cash2 = cash
    var plus = 0
    var minus = 0
    for (i in 0 until 13) {
        if (list[i] < list[i + 1]) {
            plus++
            minus = 0
        } else if (list[i] > list[i + 1]) {
            minus++
            plus = 0
        }
        if (plus == 3) {
            if (sun > 0) {
                cash2 += sun * list[i + 1]
                cash2 = 0
                plus = 0
                minus = 0
            }
        }
        if (minus == 3) {
            if (list[i] <= cash2) {
                var a = (cash2 / list[i + 1])
                cash2 -= (a * list[i + 1])
                sun += a
                minus = 0
                plus = 0
            }
        }
    }

    // 계산
    var jun_f = (cash1 + list[13] * jun)
    var sun_f = (cash2 + list[13] * sun)

    if (jun_f > sun_f) {
        println("BNP")
    } else if (jun_f < sun_f) {
        println("TIMING")
    } else {
        println("SAMESAME")
    }
}