import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    int[][] graph;
    boolean[][] visited;
    int n, m ;
    int[] answer = new int[2];

    public void bfs(int r, int c) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{r, c});
        visited[r][c] = true;
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int count = 1;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cur_r = cur[0];
            int cur_c = cur[1];

            for (int[] dir : directions) {
                int next_r = cur_r + dir[0];
                int next_c = cur_c + dir[1];
                if (next_r >= 0 && next_r < n && next_c >= 0 && next_c < m) {
                    if (!visited[next_r][next_c] && graph[next_r][next_c] == 1) {
                        queue.add(new int[]{next_r, next_c});
                        visited[next_r][next_c] = true;
                        count++;
                    }
                }
            }
        }
        answer[0]++;
        answer[1] = Math.max(count, answer[1]);
    }
    public int[] solution(int n, int m , int[][] graph) {
        this.graph = graph;
        this.n = n;
        this.m = m;
        visited = new boolean[n][m];

        for (int i = 0 ; i < n ; i++) {
            for (int j = 0 ; j < m ; j++) {
                if (!visited[i][j] && graph[i][j] == 1) {
                    bfs(i, j);
                }
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

        int[][] graph = new int[n][m];

        for (int i = 0 ; i < n ; i++) {
            for (int j = 0 ; j < m ; j++) {
                graph[i][j] = scanner.nextInt();
            }
        }
        scanner.close();

        int[] result = T.solution(n, m, graph);

        System.out.println(result[0]);
        System.out.println(result[1]);
    }
}
