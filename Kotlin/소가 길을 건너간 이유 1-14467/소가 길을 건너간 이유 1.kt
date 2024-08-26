fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val list = ArrayList<ArrayList<Int>>()
    repeat(10) {
        list.add(ArrayList<Int>())
    }
    var count = 0
    repeat(n) {
        var (a, b) = readLine().split(" ").map { it.toInt() }
        if (list[a - 1].isEmpty()) {
            list[a - 1].add(b)
        } else {
            if (list[a - 1].isNotEmpty() && list[a - 1][0] != b) {
                count++
                list[a - 1][0] = b

            }
        }

    }
    println(count)
}