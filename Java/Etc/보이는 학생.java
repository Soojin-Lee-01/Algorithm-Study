import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public int solution (int[] data) {
        int answer = 1;

        int temp = data[0];

        for (int i = 1 ; i < data.length; i++) {
            if (temp < data[i]) {
                answer++;
                temp = data[i];
            }
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

