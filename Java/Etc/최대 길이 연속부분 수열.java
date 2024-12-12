import java.util.Scanner;

import static java.lang.Math.max;
/*
문제 : 최대 길이 연속부분 수열
K는 0을 1로 변환할 수 있는 가능 개수
ex) 1 1 0 0 1 1 0 1 1 0 1 1 0 1 -> K = 2일 때 최대 길이는 8

Two-Pointer로 풀이

시간복잡도 : O(n)
*/
public class Main {
    public int solution(int[] data, int K) {
        int result = 0;
        int left = 0, temp = 0;

        for (int i = 0 ; i < data.length ; i++) {
            if (data[i] == 0) temp++;

            while (temp > K) {
                if (data[left] == 0) temp--;
                left++;
            }
            result = Math.max(result, i-left+1);
        }
        return result;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int K = scanner.nextInt();
        int[] data = new int[num];

        for (int i = 0 ; i < num ; i ++) {
            int temp = scanner.nextInt();
            data[i] = temp;
        }
        System.out.println(T.solution(data, K));
    }
}
