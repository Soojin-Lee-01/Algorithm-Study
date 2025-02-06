import java.io.*;
import java.util.*;

public class Main {
    public int solution(int n, int[] data) {
        int answer = 0;
        for (int i = 0 ; i < n-1 ; i++) {
            int temp = data[i];
            for (int j = i + 1; j < n ; j++) {
                int cal = temp ^ data[j];
                int count = Integer.bitCount(cal);

                if (count <= 2) answer++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        scanner.nextLine();

        int[] data = new int[n];
        for (int i = 0 ; i < n ; i++) {
            // 2진수를 10진수로 변환
            data[i] = Integer.parseInt(scanner.nextLine(),2);
        }

        scanner.close();

        System.out.println(T.solution(n, data));
    }
}
