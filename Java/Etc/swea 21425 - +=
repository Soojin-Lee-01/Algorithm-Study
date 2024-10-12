import java.util.*;

public class Main {
    public int solutions(int a, int b, int n) {
        int answer = 0;

        while (a <= n && b <= n) {
            if (a < b) {
                a += b;
            } else {
                b += a;
            }
            answer++;
        }

        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        for (int i = 0 ; i < num ; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int n = scanner.nextInt();

            System.out.println(T.solutions(a, b, n));
        }
    }
}
