import java.util.Scanner;
import java.util.Stack;

// peek() -> 맨 뒤에 있는 것 그냥 확인, pop() -> 맨 뒤에 있는 것 가져옴
public class Main {
    public int solution(int[][]graph, int[] moves) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        for (int m : moves) {
            for (int i = 0 ; i < graph.length ; i++) {
                if (graph[i][m-1] != 0) {
                    if (stack.isEmpty()) {
                        stack.add(graph[i][m-1]);
                    } else {
                        if (stack.peek() == graph[i][m-1]) {
                            stack.pop();
                            answer += 2;
                        } else stack.add(graph[i][m-1]);
                    }
                    graph[i][m-1] = 0;
                    break;
                }
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        int n = scanner.nextInt();
        int[][] graph = new int[n][n];
        for (int i = 0 ; i < n ; i++) {
            for (int j  = 0 ; j < n ; j++) {
                int data = scanner.nextInt();
                graph[i][j] = data;
            }
        }
        int move = scanner.nextInt();
        int[] moves = new int[move];
        for (int i = 0 ; i < moves.length; i++) {
            moves[i] = scanner.nextInt();
        }
        System.out.println(T.solution(graph, moves));
    }
}
