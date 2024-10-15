import java.util.*;

public class Main {
    public int solution(int[] data) {
        int answer = 0;
        int count = 0;
        for (int i = 0 ; i < data.length ; i++) {
            if (data[i] == 1) {
                count++;
                answer += count;
            } else count = 0;
        }
        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] data = new int[n];

        for (int i = 0 ; i < n ; i++) {
            int num = scanner.nextInt();
            data[i] = num;
        }
        System.out.println(T.solution(data));
    }
}
