import java.util.*;

public class Main {
    // 시간복잡도 : O(n log n)
    public int solution(int n) {
        int answer = 0;
        int[] data = new int[n+1];

        for (int i = 2 ; i < n+1 ; i++) {
            if (data[i] == 0) {
                answer++;
                for (int j = i ; j < n+1 ; j = j+i) {
                    data[j] = 1;
                }
            }
        }
        return answer;
    }
    public static void main(String[] args) {
       Main T = new Main();
       Scanner scanner = new Scanner(System.in);
       int n = scanner.nextInt();
       System.out.println(T.solution(n));
    }
}
