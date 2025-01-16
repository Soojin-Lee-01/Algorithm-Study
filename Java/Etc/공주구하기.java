/*
문제 : 공주 구하기

N명의 왕자가 K번을 외치면 탈락!
탈락하면 다음 왕자는 1번 왕자가 된다.

answer : 마지막에 남는 사람은 몇번 왕자?

[IDEA]
- Queue 를 이용한다.
- K-1 번 동안 맨앞 pop 하고 뒤에 push!
- 그리고 K 번째 사람은 아예 pop
- 이것을 반복하며 최후의 남는 사람을 구한다.
*/
import java.util.*;

public class Main{
    public int solution (int N, int K) {
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1 ; i < N + 1 ; i++) {
            queue.offer(i);
        }
        while (true) {
            if (queue.size() == 1) break;
            else {
                for (int j = 0; j < K - 1; j++) {
                    queue.offer(queue.poll());
                }
                queue.poll();
            }
        }
        return queue.peek();
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        int N = scanner.nextInt();
        int K = scanner.nextInt();

        System.out.println(T.solution(N, K));
    }
}
