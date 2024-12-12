import java.util.Scanner;
/*
문제 : 연속된 자연수의 합 (연속된 2개 이상의 자연수)
ex) N = 15 -> (1+2+3+4+5+), (4+5+6), (7+8) : 3개
Math로 풀이

시간복잡도 : O(n)
*/
public class Main {
    public int solution(int sum) {
        int result = 0;
        int cnt = 1;
        sum -= 1;
        /*
        <수학으로 풀이>
        - (7, 8) -> 15에서 3을 빼고 나누기 2 진행 시 나머지 x result += 1 
        */

        while (sum > 0) {
            cnt ++;
            sum -= cnt;
            if (sum % cnt == 0) result++;
        }

        return result;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        System.out.println(T.solution(num));
    }
}
