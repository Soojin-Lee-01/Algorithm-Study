import java.util.*;

import static java.lang.System.in;

public class Main {
    // two pointer 풀이 - O(n)
    public int solution(int N, int K, ArrayList<Integer> data) {
        int answer = 0;

        int p1 = 0;
        int p2 = 0;
        int count = 0;
        int temp = 0;
        while (p2 < data.size()) {
            if (count == K) {
                if (answer < temp) {
                    answer = temp;
                    temp -= data.get(p1++);
                    count -= 1;
                } else {
                  temp -= data.get(p1++);
                  count -= 1;
                }
            } else {
                temp += data.get(p2);
                p2++;
                count += 1;
            }

        }
        return answer;
    }
    // sliding window 풀이 - O(n)
    public int solution2(int N, int K, ArrayList<Integer> data) {
        int answer = 0;
        int sum = 0;
        for (int i = 0 ; i < K ; i ++) sum += data.get(i);
        answer = sum;
        for (int i = K ; i < N ; i++) {
            sum += (data.get(i) - data.get(i-K));
            answer = Math.max(answer, sum);
        }
        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();
        ArrayList<Integer> data = new ArrayList<>();

        for (int i = 0 ; i < N ; i ++) {
            int num = scanner.nextInt();
            data.add(num);
        }

        System.out.println(T.solution2(N, K,data));
    }
}
