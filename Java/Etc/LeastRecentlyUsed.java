/*
문제 : LRU
정렬 문제!

캐시 히트, 캐시 미스를 생각해서 정렬을 해준다.

1) 만약 캐시 미스가 난다면,
-> 끝부터 처음까지 한 칸씩 뒤로 미루고, 맨 앞에 데이터 삽입
2) 만약 캐시 히트가 난다면,
-> 그 자리 -1 부터 처음까지 한 칸씩 뒤로 미루고, 맨 앞에 데이터 삽입
*/
import java.util.*;

public class Main{

    public int[] solution(int n, int[] data) {
        int[] answer = new int[n];
        for (int x : data) {
            int pos = -1;
            for (int i = 0 ; i < n ; i ++) if (x == answer[i]) pos = i;
            if (pos == -1) {
                for (int j = n-1 ; j >= 1 ; j--) {
                    answer[j] = answer[j-1];
                }
            }
            else {
                for (int j = pos ; j >= 1 ; j--) {
                    answer[j] = answer[j-1];
                }
            }
            answer[0] = x;
        }
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        int n = scanner.nextInt();
        int num = scanner.nextInt();

        int[] data = new int[num];

        for (int i = 0 ; i < num ; i++) {
            data[i] = scanner.nextInt();
        }
        for (int k : T.solution(n, data)) {
            System.out.print(k + " ");
        }
    }
}
