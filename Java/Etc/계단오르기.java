import java.util.Scanner;

public class Main {
    static int[] dy;
    public int solution(int n) {
        dy[1] = 1;
        dy[2] = 2;
        for (int i = 3 ; i <=n ; i++) {
            dy[i] = dy[i-2] + dy[i-1];
        }
        return dy[n];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        int num = scanner.nextInt();
        scanner.close();
        dy = new int[num+1];
        System.out.println(T.solution(num));
    }
}
