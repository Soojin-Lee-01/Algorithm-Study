import java.util.*;

public class Main {
    public int solution(int[][] graph) {
        int answer = 0;
        int[][] directions = new int[4][2];
        directions = new int[][]{{1, 0}, {0, 1}, {0, -1}, {-1, 0}};

        for (int i = 0 ; i < graph.length; i++) {
            for (int j = 0 ; j < graph.length ; j++) {
                int x = i;
                int y = j;
                int count = 0;
                for (int k = 0 ; k < 4 ; k++) {
                    int next_r = x + directions[k][0];
                    int next_c = y + directions[k][1];

                    if (next_r >= 0 && next_r < graph.length && next_c >= 0 && next_c < graph.length ) {
                        if (graph[x][y] > graph[next_r][next_c]) count++;
                    } else {
                        count++;
                    }
                }
                if (count == 4) answer += 1;
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] graph = new int[n][n];
        for (int i = 0 ; i < n ; i ++) {
            for (int j = 0 ; j < n ; j++) {
                int num = scanner.nextInt();
                graph[i][j] = num;
            }
        }
        System.out.print(T.solution(graph));

    }
}
