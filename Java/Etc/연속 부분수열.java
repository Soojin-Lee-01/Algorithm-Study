import java.util.*;

public class Main {
    public int solution(int N, int M , int[]data) {
        int answer = 0;
        int p1 = 0;
        int p2 = 0;
        int temp = data[0];
        while (p2 < N) {
            if (temp == M) {
                answer += 1;
                p2++;
                if (p2 == N) break;
                temp += data[p2];
            } else if (temp < M) {
                p2++;
                if (p2 == N) break;
                temp += data[p2];
            } else {
                temp -= data[p1];
                p1++;
            }

        }

        return answer;
    }
  
    public int solution2(int N, int M, int[] data) {
        int answer = 0, sum = 0, lt = 0;
        for (int rt = 0; rt < N ; rt++) {
            sum += data[rt];
            if (sum == M) answer++;
            while (sum >= M) {
                sum -= data[lt++];
                if (sum == M) answer++;
            }
        }

        return answer;
    }
  
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int[] data = new int[N];
        for (int i = 0 ; i < N ; i++) {
            int num = scanner.nextInt();
            data[i] = num;
        }

        System.out.println(T.solution2(N, M, data));

    }
}

