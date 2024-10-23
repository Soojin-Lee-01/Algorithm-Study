import java.util.*;

public class Main {
    public static int solution(int n, PriorityQueue<Integer> data) {
        int answer = 0;

        while (data.size() > 1) {
            int data1 = data.poll();
            int data2 = data.poll();
            int sum = data1 + data2;
            answer += sum;
            data.add(sum);
        }
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PriorityQueue<Integer> data = new PriorityQueue<>();
        int n = scanner.nextInt();
        for (int i = 0 ; i < n ;i++) {
            int num = scanner.nextInt();
            data.add(num);
        }
        System.out.println(solution(n, data));
    }
}
