import java.util.*;

public class Main {
    public int solution(int num, int[][] graph) {
        int answer = 0, max = Integer.MIN_VALUE;

        for (int i = 0 ; i < num ; i++) {
            int count = 0;
            for (int j = 0 ; j < num ; j++) {
                for (int k = 0 ; k < 5 ; k++) {
                    if (graph[i][k] == graph[j][k]) {
                        count++;
                        break;
                    }
                }
            }
            if (count > max) {
                max = count;
                answer = i;
            }
        }
        return answer + 1;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int[][] graph = new int[num][5];

        for (int i = 0 ; i < num ; i++) {
            for (int j = 0 ; j < 5 ; j++) {
                int n = scanner.nextInt();
                graph[i][j] = n;
            }
        }
        System.out.println(T.solution(num, graph));
    }
}
