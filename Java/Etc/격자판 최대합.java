import java.util.*;

public class Main {
    public int solution (int[][] graph) {
        int answer = Integer.MIN_VALUE;
        int sum1, sum2;
        for (int i = 0 ; i < graph.length ; i++) {
            sum1 = sum2 = 0;
            for (int j = 0 ; j < graph.length ; j++) {
                sum1 += graph[i][j];
                sum2 += graph[j][i];
            }
            answer = Math.max(answer, sum1);
            answer = Math.max(answer, sum2);
        }
        sum1 = sum2 = 0;
        for (int i = 0 ; i < graph.length ; i++) {
            sum1 += graph[i][i];
            sum2 += graph[i][graph.length-i-1];
        }
        answer = Math.max(answer, sum1);
        answer = Math.max(answer, sum2);

        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] graph = new int[n][n];
        for (int i = 0 ; i < n ; i++) {
            for (int j = 0 ; j < n ; j ++) {
                int num = scanner.nextInt();
                graph[i][j] = num;
            }
        }
        System.out.print(T.solution(graph));
    }
}
