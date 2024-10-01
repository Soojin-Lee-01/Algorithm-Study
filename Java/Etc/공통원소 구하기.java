import java.util.*;

import static java.lang.System.in;

public class Main {

    public ArrayList<Integer> solution(int N, int M, int[] data1, int[] data2) {
        ArrayList<Integer> answer = new ArrayList<>();
        int p1 = 0, p2 = 0;
        Arrays.sort(data1);
        Arrays.sort(data2);

        while (p1 < N && p2 < M) {
            if (data1[p1] == data2[p2]) {
                answer.add(data1[p1++]);
                p2++;
            } else if (data1[p1] < data2[p2]) {
                p1++;
            } else {
                p2++;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] data1 = new int[N];
        for (int i = 0 ; i < N ; i++) {
            int num = scanner.nextInt();
            data1[i] = num;
        }
        int M = scanner.nextInt();
        int[] data2 = new int[M];
        for (int i = 0 ; i < M ; i++) {
            int num = scanner.nextInt();
            data2[i] = num;
        }

        for (int x : T.solution(N, M, data1, data2)) {
            System.out.print(x+ " ");
        }

    }
}

