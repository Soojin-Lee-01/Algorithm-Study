import java.util.*;

public class Main {
    public int[] solution(int[] data) {
        int[] answer = new int[data.length];

        for (int i = 0 ; i < data.length ; i++) {
            int temp = 1;
            for (int j = 0 ; j < data.length ; j++) {
                if (data[i] < data[j]) temp++;
            }
            answer[i] = temp;
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
        for (int k : T.solution(data)) {
            System.out.print(k + " ");
        }
    }
}
